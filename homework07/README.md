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
