Setup Kubernetes client and Socks-Shop microservice 

1.1 install minikube on Windows - installed the Win installer

1.2 Start minikube
minikube start

Failed

Solution: added minikube in PATH User Variables 

2. Setup Socks Shop application

2.1 Clone the microservices-demo repo
git clone https://github.com/microservices-demo/microservices-demo

2.2 Start the app via docker-compose

- Check the app on http://localhost/ 

2.3 Assign memory for minikube to run properly


2.4 Create the logging manifests

2.5 Check Kibana dashboard at http://192.168.99.100:31601

"Site can't be reached"


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
  
  Solution : Edit elasticsearch.yml :
  
    env: 
          - name: discovery.type
            value: single-node
			
Then deploy again manifests-loggin

		
2.6 check http://192.168.99.100:31601
 Site not working

Solution:  Finding the local IP opened :
minikube service --namespace=kube-system  kibana --url
* Starting tunnel for service kibana.
|-------------|--------|-------------|------------------------|
|  NAMESPACE  |  NAME  | TARGET PORT |          URL           |
|-------------|--------|-------------|------------------------|
| kube-system | kibana |             | http://127.0.0.1:58541 |
|-------------|--------|-------------|------------------------|

	
