# Kubernetes Homework05 Responses

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

2. I checked the logs of the pod and the ouput was what was expected.
```
[rhea1228@isp02 hw05]$ kubectl logs hello-hw-b
Hello,
Rhea
```

3. I deleted the pods using ```kubectl delete pods hello-hw-b```

## **PART C:**
1. I used the file ```my-deployment.yml``` for this part of the homework and to create the deployment I used the command ```kubectl apply -f my-deployment.yml```

2. I called the pods and got their respective ip addresses by using the ```-o wide``` tag
```
[rhea1228@isp02 hw05]$ kubectl get pods -o wide
NAME                                   READY   STATUS    RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
hello-hw-deployment-5d6bd67697-6btb9   1/1     Running   0          6m34s   10.244.3.127   c01    <none>           <none>
hello-hw-deployment-5d6bd67697-fgbss   1/1     Running   0          5m8s    10.244.4.117   c02    <none>           <none>
hello-hw-deployment-5d6bd67697-x9k5q   1/1     Running   0          5m8s    10.244.5.72    c04    <none>           <none>
```

3. I checked the logs of the pod and the ouput was what was expected.
```
[rhea1228@isp02 hw05]$ kubectl logs hello-hw-deployment-5d6bd67697-6btb9
Hello, Rhea from IP 10.244.3.127
[rhea1228@isp02 hw05]$ kubectl logs hello-hw-deployment-5d6bd67697-fgbss
Hello, Rhea from IP 10.244.4.117
[rhea1228@isp02 hw05]$ kubectl logs hello-hw-deployment-5d6bd67697-x9k5q
Hello, Rhea from IP 10.244.5.72
```
