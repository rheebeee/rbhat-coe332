## **PART A:**
1. I used the file ```my-pod.yml``` for this part of the homework and to create the pod I used the command ```kubectl apply -f my-pod.yml```

2. I called the pod using the appropriate selector
```
[rhea1228@isp02 hw05]$ kubectl get pods  --selector "greeting=personalized"
NAME       READY   STATUS    RESTARTS   AGE
hello-hw   1/1     Running   0          21m
```

3. I checked the logs of the pod and the ouput was what was expected because we didn't assign a value for the environment variable name. 
```
[rhea1228@isp02 hw05]$ kubectl logs hello-hw
Hello,
```

4. I deleted the pods using ```kubectl delete pods hello-hw```

## **PART B:**
1. I used the file ```my-pod2.yml``` for this part of the homework and to create the pod I used the command ```kubectl apply -f my-pod2.yml```

2. I checked the logs of the pod and the ouput was what was expected
```
[rhea1228@isp02 hw05]$ kubectl logs hello-hw-b
Hello,
Rhea
```

3. I deleted the pods using ```kubectl delete pods hello-hw-b```

## **PART C:**
1. I used the file ```my-deployment.yml``` for this part of the homework and to create the deployment I used the command ```kubectl apply -f my-pod2.yml```

2. I checked the logs of the pod and the ouput was what was expected
```

```

3. I deleted the pods by scalng down ```replicas: 1``` and then using the command ```kubectl delete pods hello-hw-deployment```

