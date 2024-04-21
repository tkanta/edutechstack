cd /usercode
kubectl taint node --all node-role.kubernetes.io/master-

# create the namespace to run the apiserver in
kubectl create ns wardle

# create the service account used to run the server
kubectl create -f artifacts/example/sa.yaml -n wardle

# create the rolebindings that allow the service account user to delegate authz back to the kubernetes master for incoming requests to the apiserver
kubectl create -f artifacts/example/auth-delegator.yaml -n kube-system
kubectl create -f artifacts/example/auth-reader.yaml -n kube-system

# create rbac roles and clusterrolebinding that allow the service account user to use admission webhooks
kubectl create -f artifacts/example/rbac.yaml
kubectl create -f artifacts/example/rbac-bind.yaml

# create the service and replication controller
kubectl create -f artifacts/example/deployment.yaml -n wardle
kubectl create -f artifacts/example/service.yaml -n wardle

# create the apiservice object that tells kubernetes about your api extension and where in the cluster the server is located
kubectl create -f artifacts/example/apiservice.yaml