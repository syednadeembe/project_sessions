###for generating sample yaml file
kubectl run nginx --image=nginx --dry-run=client -oyaml
###for debugging 
kubectl debug -it myapp --image=ubuntu --share-processes --copy-to=myapp-base