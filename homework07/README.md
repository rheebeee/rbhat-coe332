# Homework07 Responses

## **Part A:**
1. Building the image and pushing it into docker hub
```
[rhea1228@isp02 hw06]$ docker build -t rheebeee/animals-service-final .
[rhea1228@isp02 hw06]$ docker push rheebeee/animals-service-final
```

2. I curled the IP address of my flask service 
```
[rhea1228@isp02 hw07]$ kubectl get services
NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
rhea1228-hw07-test-flask   ClusterIP   10.111.21.121    <none>        5000/TCP         8h
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
root@rhea1228-test-redis-debug-5c79b45878-sp4jp:/data# curl -X POST -H "content-type:       application/json" -d '{"start": "START", "end": "END"}' 10.244.13.93:5000/jobs
{"id": "f8ba95eb-8fd3-46d9-9b19-01c46442ea79", "status": "submitted", "start": "START", "end": "END"}

root@rhea1228-test-redis-debug-5c79b45878-sp4jp:/data# python3
>>> import redis
>>> rd = redis.StrictRedis(host='10.109.236.250', port=6379, db=0)
>>> rd.keys()
[b'job.f8ba95eb-8fd3-46d9-9b19-01c46442ea79', b"job.b'f8ba95eb-8fd3-46d9-9b19-01c46442ea79'", b"job.b'cf159ce5-f692-4e21-8a42-f10a80277c46'", b'job.cf159ce5-f692-4e21-8a42-f10a80277c46']

>>> rd.hget('job.f8ba95eb-8fd3-46d9-9b19-01c46442ea79',b'status')
b'submitted'

```

(b)



## **Part B:**
1. I updated my worker deployment
```
[rhea1228@isp02 hw07]$ kubectl apply -f rhea1228-hw7-worker-deployment.yml
deployment.apps/rhea1228-hw7-worker-deployment configured
```


## **Part C:**
```
[rhea1228@isp02 hw06]$ 
```
