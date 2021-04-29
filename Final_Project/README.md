# Final Project: Traffic Data

## **Building the Files**

1. Build the docker images & push them to DokerHub
```
[rhea1228@isp02 hw06]$ docker build -t rheebeee/traffic02-service .
[rhea1228@isp02 hw06]$ docker push rheebeee/traffic02-service
```
2. Build & run the Kubernetes files
```
[rhea1228@isp02 hw06]$ kubectl apply -f traffic02-test-flask-service.yml
[rhea1228@isp02 hw06]$ kubectl apply -f traffic02-test-redis-deployment.yml
[rhea1228@isp02 hw06]$ kubectl apply -f traffic02-test-redis-pvc.yml
[rhea1228@isp02 hw06]$ kubectl apply -f traffic02-test-redis-service.yml
[rhea1228@isp02 hw06]$ kubectl apply -f traffic02-api-deployment.yml
```

3. Exec to the Kubernetes container & install the needed dependencies
```
[rhea1228@isp02 hw06]$ kubectl exec -it traffic02-test-redis-deployment-7b7fc4667c-227rq -- /bin/bash
root@traffic02-worker-deployment-5df7b7bc78-ps6kk:/api# apt-get update && apt-get install -y python3
root@traffic02-worker-deployment-5df7b7bc78-ps6kk:/api# apt-get install python3-pip
root@traffic02-worker-deployment-5df7b7bc78-ps6kk:/api# pip3 install redis
root@traffic02-worker-deployment-5df7b7bc78-ps6kk:/api# pip3 install ipython
```

4. Check the IP address of the services. The ```traffic02-test-flask``` service IP is used for the curl statements and the ```traffic02-test-redis``` service IP is used for the queue and redis databases within the ```jobs.py``` file

```
[rhea1228@isp02 final_proj2]$ kubectl get services
NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
traffic02-test-flask       ClusterIP   10.99.161.74     <none>        5000/TCP         4d5h
traffic02-test-redis       ClusterIP   10.105.231.136   <none>        6379/TCP         4d5h
```

5. First, reset the database
```
root@traffic02-worker-deployment-5df7b7bc78-ps6kk:/api# curl 10.99.161.74:5000/reset
```

2. I used the following commands to set my redis keys:
```
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# python3
Python 3.5.3 (default, Apr  5 2021, 09:00:41)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import redis
>>> rd_data= redis.StrictRedis(host= '10.105.231.136', port=6379, db=2, decode_responses= True)
>>> rd_jobs = redis.StrictRedis(host= '10.105.231.136', port=6379, db=0)
>>> 
>>> rd.keys()

```


