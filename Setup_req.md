# Setup Kubernetes client  

install minikube on Windows - installed the Win installer

Start minikube
```
minikube start
```
Failed

Solution: added minikube in PATH User Variables 

# Setup  Socks-Shop microservice 
## Deploy on Docker

Clone the microservices-demo repo
```
git clone https://github.com/microservices-demo/microservices-demo
```
Start the app via docker-compose

Check the app on http://localhost/ 

## Deploy on Kubernetes
Assign memory for minikube to run properly
```
minikube start --memory 8192 --cpus 4
```
Create the logging manifests
```
kubectl create -f deploy/kubernetes/manifests-logging
```


Find local minikube IP then check Kibana dashboard

Not working, below see the troubleshooting steps

```
kubectl get deployment --namespace=kube-system
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
coredns         1/1     1            1           12m
elasticsearch   0/1     1            0           3m45s
kibana          0/1     1            0           3m45s

kubectl get pods --namespace=kube-system
NAME                               READY   STATUS             RESTARTS   AGE
coredns-74ff55c5b-t2sfk            1/1     Running            0          12m
elasticsearch-667c4b54b8-84mzv     0/1     ImagePullBackOff   0          4m51s
etcd-minikube                      1/1     Running            0          13m
fluentd-j45db                      1/1     Running            0          4m50s
kibana-5cf9b7f46f-jw7kz            0/1     ImagePullBackOff   0          4m51s
kube-apiserver-minikube            1/1     Running            0          13m
kube-controller-manager-minikube   1/1     Running            0          13m
kube-proxy-dfmcf                   1/1     Running            0          12m
kube-scheduler-minikube            1/1     Running            0          13m
storage-provisioner                1/1     Running            1          13m


kubectl describe pod elasticsearch-667c4b54b8-84mzv --namespace=kube-system
Name:         elasticsearch-667c4b54b8-84mzv
Namespace:    kube-system
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Tue, 11 May 2021 13:22:54 +0100
Labels:       name=elasticsearch
              pod-template-hash=667c4b54b8
Annotations:  <none>
Status:       Pending
IP:           172.17.0.3
IPs:
  IP:           172.17.0.3
Controlled By:  ReplicaSet/elasticsearch-667c4b54b8
Containers:
  elasticsearch:
    Container ID:
    Image:          elasticsearch
    Image ID:
    Port:           9200/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-fq5q6 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  default-token-fq5q6:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-fq5q6
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  beta.kubernetes.io/os=linux
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  5m44s                  default-scheduler  Successfully assigned kube-system/elasticsearch-667c4b54b8-84mzv to minikube
  Normal   Pulling    4m2s (x4 over 5m42s)   kubelet            Pulling image "elasticsearch"
  Warning  Failed     4m (x4 over 5m40s)     kubelet            Failed to pull image "elasticsearch": rpc error: code = Unknown desc = Error response from daemon: manifest for elasticsearch:latest not found: manifest unknown: manifest unknown
  Warning  Failed     4m (x4 over 5m40s)     kubelet            Error: ErrImagePull
  Warning  Failed     3m36s (x7 over 5m39s)  kubelet            Error: ImagePullBackOff
  Normal   BackOff    33s (x20 over 5m39s)   kubelet            Back-off pulling image "elasticsearch"
  ```
 
 Docker hub - no latest tag for both elasticsearch and kibana images
 Solution:  updated the yaml files to include a fixed version
 
 ```
 Events:
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  2m54s                default-scheduler  Successfully assigned kube-system/elasticsearch-69d8bb74cf-p9nz9 to minikube
  Normal   Pulled     50s (x4 over 2m53s)  kubelet            Container image "elasticsearch:7.12.1" already present on machine
  Normal   Created    50s (x4 over 2m53s)  kubelet            Created container elasticsearch
  Normal   Started    50s (x4 over 2m53s)  kubelet            Started container elasticsearch
  Warning  BackOff    4s (x6 over 116s)    kubelet            Back-off restarting failed container

kubectl logs  --namespace=kube-system elasticsearch-69d8bb74cf-p9nz9

...
 the default discovery settings are unsuitable for production use; at least one of [discovery.seed_hosts, discovery.seed_providers, cluster.initial_master_nodes] must be configured
 ```
 Solution : Edit elasticsearch.yml :
  ```
    env: 
          - name: discovery.type
            value: single-node
```		
Then deploy again manifests-logging

		
Check Kibana dashboard on local IP

 *This site can’t be reached*

Solution:  start minikube tunnel to Kibana :
```
minikube service --namespace=kube-system  kibana --url
* Starting tunnel for service kibana.
|-------------|--------|-------------|------------------------|
|  NAMESPACE  |  NAME  | TARGET PORT |          URL           |
|-------------|--------|-------------|------------------------|
| kube-system | kibana |             | http://127.0.0.1:58541 |
|-------------|--------|-------------|------------------------|
```
Deploy socks-shop on minikube
```
kubectl create -f deploy/kubernetes/manifests

```
Test the microservice deployment-front-end

```
minikube service front-end --namespace=sock-shop --url
* Starting tunnel for service front-end.
|-----------|-----------|-------------|------------------------|
| NAMESPACE |   NAME    | TARGET PORT |          URL           |
|-----------|-----------|-------------|------------------------|
| sock-shop | front-end |             | http://127.0.0.1:61706 |
|-----------|-----------|-------------|------------------------|
http://127.0.0.1:61706
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```


