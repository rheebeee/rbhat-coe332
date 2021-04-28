# Kubernetes Homework06 Responses

## **Steps 1-3:**

```
[rhea1228@isp02 hw06]$ kubectl apply -f rhea1228-test-redis-pvc.yml
[rhea1228@isp02 hw06]$ kubectl apply -f rhea1228-test-redis-deployment.yml
[rhea1228@isp02 hw06]$ kubectl apply -f rhea1228-test-redis-service.yml
```

## **Steps 1-3: Checking My Work**
1. I used the following commands to install my depdendencies:
```
[rhea1228@isp02 hw06]$ kubectl exec -it rhea1228-test-redis-debug-5c79b45878-jbhmq -- /bin/bash
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# apt-get update && apt-get install -y python3
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# apt-get install python3-pip
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# pip3 install redis
```
2. I used the following commands to set my redis keys:
```
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# python3
Python 3.5.3 (default, Apr  5 2021, 09:00:41)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import redis
>>> rd = redis.StrictRedis(host='10.109.236.250', port=6379, db=0)
>>> rd.keys()
>>> rd.set('my_key','my_value')
True
>>> rd.keys()
[b'my_key']
```



## **Step 4:**
```
[rhea1228@isp02 hw06]$ kubectl  apply -f rhea1228-test-flask-deployment.yml
[rhea1228@isp02 hw06]$ kubectl apply -f rhea1228-test-flask-service.yml

[rhea1228@isp02 hw04]$ docker build -t rheebeee/test_image .
[rhea1228@isp02 hw04]$ docker push rheebeee/test_image
```
