###prerequirement : you have the Images created from the previous sessions project_sessions/session-3/part-2
###for generating sample yaml file
kubectl run myapp --image=nginx --dry-run=client -oyaml 
###replica set & when to use it
###deployment and when to use it
kubectl create deployment myapp-baseimage-deploy --image=myapp:baseImage --dry-run=client -ojson
kubectl create deployment myapp-baseimage-deploy --image=myapp:baseImage
###explore set / rollout / scale command
kubectl get pods -n default -o jsonpath='{range .items[*]}{@.metadata.name}{" "}{@.spec.containers[*].image}{"\n"}{end}'| column -t
kubectl set image deployment/myapp-baseimage-deploy myapp=myapp:productionImage
kubectl rollout history deployment/myapp-baseimage-deploy --revision=<revision_no>
kubectl scale --replicas=2 deployment/myapp-baseimage-deploy
###understand how does loadbalancing work when we scale
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

###to be done after the design session
###for debugging explore debug / attach commands
kubectl debug -it myapp --image=ubuntu --share-processes --copy-to=myapp-base



