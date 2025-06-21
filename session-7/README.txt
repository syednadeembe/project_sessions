### create the Images with docker compose file
docker-compose build --no-cache

docker tag myapp:productionImage_ui syednadeembe/myflaskapp:productionImage_ui
docker tag myapp:productionImage_app syednadeembe/myflaskapp:productionImage_app

docker push syednadeembe/myflaskapp:productionImage_ui
docker push syednadeembe/myflaskapp:productionImage_app

### deploy netpol first 
kubectl apply -f  deployment_yamls/netpol.yaml

### deploy rbac
kubectl apply -f  deployment_yamls/rbac.yaml

### deploy database
kubectl apply -f  deployment_yamls/dbase.yaml

### login to database 
kubectl exec -it <mongo pod> bash

mongosh -u root -p root

test> show databases
admin   156.00 KiB
config   60.00 KiB
local    72.00 KiB

use admin
admin> show collections
admin> db.usage.find().pretty()


### deploy application
kubectl apply -f  deployment_yamls/app.yaml

### deploy UI
kubectl apply -f  deployment_yamls/ui.yaml

### secure-dbase-credentials
kubectl delete -f deployment_yamls/dbase.yaml

### create a mount folder on the local that pv can use, update the template with your location and also give k8s permission on the folder
kubectl apply -f deployment_yamls/secure_dbase_deployment/pv.yaml
kubectl apply -f deployment_yamls/secure_dbase_deployment/dbase.yaml
