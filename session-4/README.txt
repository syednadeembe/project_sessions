###for generating sample yaml file
kubectl run nginx --image=nginx --dry-run=client -oyaml
###explore patch / scale command
###understand difference b/w service and endpoints
###why service has to be created and endpoints are auto-created
###for debugging explore debug / attach commands
kubectl debug -it myapp --image=ubuntu --share-processes --copy-to=myapp-base
