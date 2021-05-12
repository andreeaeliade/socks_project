# socks_project
This python program deployments.py uses Kubernetes API to provide the following information:

- name of deployments
- images of each deployments
- date deployment was updated

## Requirements 

Kubernetes client and Socks-Shop microservice requirements - more info [here](https://github.com/andreeaeliade/socks_project/blob/main/Setup_req.md)

Install Python 2.7 or 3.5+
Install Kubernetes client
```
pip install kubernetes
```
 ## Running the script 
```
python deployments.py
```

The command will list all deployments for all namespaces
```
List deployments for all namespaces

NAME         DATE                       IMAGES
coredns      2021-05-11 21:37:44+00:00  k8s.gcr.io/coredns:1.7.0
carts        2021-05-11 21:39:02+00:00  weaveworksdemos/carts:0.4.8
carts-db     2021-05-11 21:39:57+00:00  mongo
catalogue    2021-05-11 21:45:44+00:00  weaveworksdemos/catalogue:0.3.5
catalogue-db 2021-05-11 21:40:30+00:00  weaveworksdemos/catalogue-db:0.3.0
front-end    2021-05-11 21:41:13+00:00  weaveworksdemos/front-end:0.3.12
orders       2021-05-12 08:35:42+00:00  weaveworksdemos/orders:0.4.7
orders-db    2021-05-11 21:40:40+00:00  mongo
payment      2021-05-11 21:45:38+00:00  weaveworksdemos/payment:0.4.3
queue-master 2021-05-12 08:36:23+00:00  weaveworksdemos/queue-master:0.3.1
rabbitmq     2021-05-11 21:42:50+00:00  rabbitmq:3.6.8-management
                                        kbudde/rabbitmq-exporter
session-db   2021-05-11 21:41:22+00:00  redis:alpine
shipping     2021-05-12 08:50:33+00:00  weaveworksdemos/shipping:0.4.8
user         2021-05-11 21:44:41+00:00  weaveworksdemos/user:0.4.7
user-db      2021-05-11 21:42:32+00:00  weaveworksdemos/user-db:0.3.0
```

```
python socks.python sock-shop
```
The command will return all deployments for namespace="sock-shop"
```
List deployments for sock-shop namespace
NAME         DATE                       IMAGES
carts        2021-05-11 21:39:02+00:00  weaveworksdemos/carts:0.4.8
carts-db     2021-05-11 21:39:57+00:00  mongo
catalogue    2021-05-11 21:45:44+00:00  weaveworksdemos/catalogue:0.3.5
catalogue-db 2021-05-11 21:40:30+00:00  weaveworksdemos/catalogue-db:0.3.0
front-end    2021-05-11 21:41:13+00:00  weaveworksdemos/front-end:0.3.12
orders       2021-05-12 08:35:42+00:00  weaveworksdemos/orders:0.4.7
orders-db    2021-05-11 21:40:40+00:00  mongo
payment      2021-05-11 21:45:38+00:00  weaveworksdemos/payment:0.4.3
queue-master 2021-05-12 08:36:23+00:00  weaveworksdemos/queue-master:0.3.1
rabbitmq     2021-05-11 21:42:50+00:00  rabbitmq:3.6.8-management
                                        kbudde/rabbitmq-exporter
session-db   2021-05-11 21:41:22+00:00  redis:alpine
shipping     2021-05-12 08:50:33+00:00  weaveworksdemos/shipping:0.4.8
user         2021-05-11 21:44:41+00:00  weaveworksdemos/user:0.4.7
user-db      2021-05-11 21:42:32+00:00  weaveworksdemos/user-db:0.3.0
```
