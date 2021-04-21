# Homework07 Responses

## **Part A:**
1. Building the image and pushing it into docker hub
```
[rhea1228@isp02 hw06]$ docker build -t rheebeee/animals-service-help .
[rhea1228@isp02 hw06]$ docker push rheebeee/animals-service-help
```

2. I curled the IP address of my flask service 
```
[rhea1228@isp02 hw07]$ kubectl get services
NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
rhea1228-hw07-test-flask   ClusterIP   10.111.21.121    <none>        5000/TCP         2d7h
rhea1228-test              ClusterIP   10.109.236.250   <none>        6379/TCP         14d

```

3. I execed into my python debug container & installed my dependencies
```
[rhea1228@isp02 hw06]$ kubectl exec -it rhea1228-test-redis-debug-5c79b45878-jbhmq -- /bin/bash

root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# apt-get update && apt-get install -y curl
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# apt-get install python3-pip
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# pip3 install redis

root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# curl 10.111.21.121:5000

``` 

(a)
```
#I did multiple curl statements to create multiple keys 

root@rhea1228-test-redis-debug-5c79b45878-sp4jp:/data# curl -X POST -H "content-type:       application/json" -d '{"start": "START", "end": "END"}' 10.111.21.121:5000/jobs
{"id": "f8ba95eb-8fd3-46d9-9b19-01c46442ea79", "status": "submitted", "start": "START", "end": "END"}

root@rhea1228-test-redis-debug-5c79b45878-sp4jp:/data# python3
>>> import redis
>>> rd = redis.StrictRedis(host='10.109.236.250', port=6379, db=0)
>>> rd.keys()
[b'job.57bcf915-7eb1-4423-8851-b3c4df5b3164', b'job.ce37ba28-4eba-4b59-a48f-1a154a95e70b', b'job.3d082658-2aad-42b7-b602-ba5e0f071cc5', b"job.b'f8ba95eb-8fd3-46d9-9b19-01c46442ea79'", b"job.b'3d082658-2aad-42b7-b602-ba5e0f071cc5'", b'job.4d29a718-a325-47a5-abbc-22a3350ae19e', b'job.f8ba95eb-8fd3-46d9-9b19-01c46442ea79', b'job.975e89a0-6416-4a53-8baa-3a56bc9078d6', b'job.31039c93-28db-4e0d-9990-6d5e4b19e6b4', b'job.cf159ce5-f692-4e21-8a42-f10a80277c46', b"job.b'31039c93-28db-4e0d-9990-6d5e4b19e6b4'", b"job.b'ce37ba28-4eba-4b59-a48f-1a154a95e70b'", b"job.b'4d29a718-a325-47a5-abbc-22a3350ae19e'", b"job.b'cf159ce5-f692-4e21-8a42-f10a80277c46'", b"job.b'57bcf915-7eb1-4423-8851-b3c4df5b3164'"]
```

(b) These are my keys and their statuses
```
>>> for key in rd.keys():
...     rd.hmget(key, 'status')
...     print(key)
...
[b'submitted']
b'job.57bcf915-7eb1-4423-8851-b3c4df5b3164'
[b'submitted']
b'job.ce37ba28-4eba-4b59-a48f-1a154a95e70b'
[b'submitted']
b'job.3d082658-2aad-42b7-b602-ba5e0f071cc5'
[b'complete']
b"job.b'f8ba95eb-8fd3-46d9-9b19-01c46442ea79'"
[b'complete']
b"job.b'3d082658-2aad-42b7-b602-ba5e0f071cc5'"
[b'submitted']
b'job.4d29a718-a325-47a5-abbc-22a3350ae19e'
[b'submitted']
b'job.f8ba95eb-8fd3-46d9-9b19-01c46442ea79'
[b'complete']
b'job.975e89a0-6416-4a53-8baa-3a56bc9078d6'
[b'submitted']
b'job.31039c93-28db-4e0d-9990-6d5e4b19e6b4'
[b'submitted']
b'job.cf159ce5-f692-4e21-8a42-f10a80277c46'
[b'complete']
b"job.b'31039c93-28db-4e0d-9990-6d5e4b19e6b4'"
[b'complete']
b"job.b'ce37ba28-4eba-4b59-a48f-1a154a95e70b'"
[b'complete']
b"job.b'4d29a718-a325-47a5-abbc-22a3350ae19e'"
[b'complete']
b"job.b'cf159ce5-f692-4e21-8a42-f10a80277c46'"
[b'complete']
b"job.b'57bcf915-7eb1-4423-8851-b3c4df5b3164'"

```


## **Part B:**
1. I updated my worker deployment
```
[rhea1228@isp02 hw07]$ kubectl apply -f rhea1228-hw7-worker-deployment.yml
deployment.apps/rhea1228-hw7-worker-deployment configured
```


2. I added the functionality ```worker_ip = os.environ.get('WORKER_IP')```
and made a new method ```set_ip()``` that is called in ```worker.py```


## **Part C:**
```
[rhea1228@isp02 source]$ kubectl get pods -o wide
NAME                                              READY   STATUS    RESTARTS   AGE     IP              NODE     NOMINATED NODE   READINESS GATES
rhea1228-hw7-worker-deployment-76585f9446-hvqdr   1/1     Running   0          33m     10.244.5.193    c04      <none>           <none>
rhea1228-hw7-worker-deployment-76585f9446-t6tvb   1/1     Running   0          33m     10.244.12.128  c12      <none>           <none>


>>> for key in rd.keys():
...     rd.hmget(key, 'status')
...     print(key)
...
[b'complete']
b"job.b'31039c93-28db-4e0d-9990-6d5e4b19e6b4'"
[worker'complete']
worker"'10.244.5.193'"
[b'complete']
b"job.b'ce37ba28-4eba-4b59-a48f-1a154a95e70b'"
[worker'complete']
worker"'10.244.12.128'"
[b'complete']
b"job.b'57bcf915-7eb1-4423-8851-b3c4df5b3164'"
[worker'complete']
worker"'10.244.12.128'"

```
