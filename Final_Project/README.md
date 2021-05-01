# Final Project: Traffic Data By: Rhea Bhat

This is my final project for COE332. Within this project, I have built a REST API that utilizes a real-time dataset of traffic incidents that have occured in Austin. There are different app routes avaialable in order to create new data entries into the database, read them, update snippets, and delete old entries.

There are various components to this project:
1. A Python script to format the data
2. A Flask API front end for submitting / accessing jobs
3. A Redis database for storing the dataset
4. A Redis database for storing job information
5. A worker back-end which runs the analysis that create an image plot for the user

## **Building the Files**

1. Build the docker images & push them to DokerHub
```
[rhea1228@isp02 final_proj2]$ docker build -t rheebeee/traffic02-service .
[rhea1228@isp02 final_proj2]$ docker push rheebeee/traffic02-service
```
2. Build & run the Kubernetes files
```
[rhea1228@isp02 final_proj2]$ kubectl apply -f traffic02-test-flask-service.yml
[rhea1228@isp02 final_proj2]$ kubectl apply -f traffic02-test-redis-deployment.yml
[rhea1228@isp02 final_proj2]$ kubectl apply -f traffic02-test-redis-pvc.yml
[rhea1228@isp02 final_proj2]$ kubectl apply -f traffic02-test-redis-service.yml
[rhea1228@isp02 final_proj2]$ kubectl apply -f traffic02-api-deployment.yml
```

3. Exec to the Kubernetes container & install the needed dependencies
```
[rhea1228@isp02 final_proj2]$ kubectl exec -it traffic02-test-redis-deployment-7b7fc4667c-227rq -- /bin/bash
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

## **FLASK API:**
1. Here are the possible routes for the Traffic02 FLASK API:
```
[rhea1228@isp02 final_proj2]$ kubectl exec -it traffic02-test-redis-deployment-7b7fc4667c-227rq -- /bin/bash
root@traffic02-worker-deployment-5df7b7bc78-z9547:/api# curl 10.99.161.74:5000/
    Here are the routes:
    /           Instructions
    /jobs       Running a job where number of incidents is plotted over time [ANALYSIS]
    /joblist    Returns all the jobs in the queue
    /add        Adds a new inncident to the database [CREATE]
    /dates      Find incidents between a 'start' and 'end' date [READ]
    /edit       Edits the issue of one of the incidents [UPDATE]
    /delete     Delete an incident from the database [DELETE]
    /reset      Resets the redis database
```    

2. First, reset the database
```
root@traffic02-worker-deployment-5df7b7bc78-z9547:/api# curl 10.99.161.74:5000/reset
The database has been reset.
```
3. Here is sample output of each of the routes:
```
root@traffic02-worker-deployment-5df7b7bc78-z9547:/api# curl '10.99.161.74:5000/dates?start=2017-10-24T20:15:51.000000Z&end=2018-10-24T20:15:51.000000Z'
[
  "92640da6-f57b-4e36-bd05-fe806c22714b",
  "24ad6018-4006-40c1-8e9e-2884359f166e",
  "282eb7dc-5022-4691-9af5-4d13faa0cb45",
]

root@traffic02-worker-deployment-5df7b7bc78-z9547:/api# curl -X DELETE -d "trafficid=9c8a8ebc-fd71-49cf-918c-79f0e0cc6405" 10.99.161.74:5000/delete
Traffic ID number 9c8a8ebc-fd71-49cf-918c-79f0e0cc6405 deleted

root@traffic02-worker-deployment-5df7b7bc78-z9547:/api# curl -X POST -H "content-type: application/json" -d '{"date": "2017-10-24T15:49:00.000Z", "issue": "COLLISION", "latitude": "30.25", "longitude": "-90.21", "address": "201 E 21st St."}' 10.99.161.74:5000/add
{
  "address": "201 E 21st St.",
  "date": "2017-10-24T15:49:00.000Z",
  "id": "8ddc4f31-104b-4eb7-9621-3b7e47bdd1f9",
  "issue": "COLLISION",
  "latitude": "30.25",
  "longitude": "-90.21"
}

root@traffic02-worker-deployment-5df7b7bc78-Z9547:/api# curl '10.99.161.74:5000/edit?trafficid='a649a545-4b1c-40c1-815a-c634c28c96d1'&issue='BREAK''
Traffic ID a649a545-4b1c-40c1-815a-c634c28c96d1 issue has been changed to BREAK

```
## **Redis Database:**
1. I used the following commands to view my redis database:

```
root@rhea1228-test-redis-debug-5c79b45878-jbhmq:/data# python3
Python 3.5.3 (default, May  1 2021, 09:00:41)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import redis
>>> rd_data= redis.StrictRedis(host= '10.105.231.136', port=6379, db=2, decode_responses= True)
>>> rd_jobs = redis.StrictRedis(host= '10.105.231.136', port=6379, db=0)
>>> 
>>> #To get all the values in the redis database
>>> for key in rd_data.keys():
>>>   print(rd_data.hgetall(key))
>>> 
>>> #To get all the Traffic ID's  
>>> rd.keys()
```

## **Worker &  Jobs:**

