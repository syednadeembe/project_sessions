###for generating sample yaml file
kubectl run myapp --image=nginx --dry-run=client -oyaml 
###replica set & when to use it
###deployment and when to use it
kubectl create deployment myapp-baseImage-deploy --image=myapp:baseImage --dry-run=client -ojson
###explore patch / scale / set command
kubectl get pods -n default -o jsonpath='{range .items[*]}{@.metadata.name}{" "}{@.spec.containers[*].image}{"\n"}{end}'| column -t
kubectl set image deployment/myapp-deployment myapp=myapp:productionImage
kubectl patch pod myapp -p '{"spec":{"containers":[{"name":"myapp","image":"myapp:baseImage"}]}}'
kubectl rollout history deployment/myapp-deployment --revision=<revision_no>

###create a pod 
kubectl apply -f myapp-base-pod.yaml
###create a service to the pod
kubectl apply -f myapp-base-service.yaml
###explore the endpoints
kubectl get endpoints
###create another pod
kubectl apply -f myapp-base-pod-replica.yaml
###explore the endpoints
kubectl get endpoints

###understand difference b/w service and endpoints
###why service has to be created and endpoints are auto-created
kubectl create service clusterip myapp-service --tcp=9000:9000 --dry-run=client -ojson
###for debugging explore debug / attach commands
kubectl debug -it myapp --image=ubuntu --share-processes --copy-to=myapp-base



