###deploy the production deployments
kubectl apply -f example-myapp-production/deployment.yaml

###create nginx for testing
kubectl run nginx --image=nginx

###curl the myapp-production service from nginx prod
kubectl exec -it nginx bash
curl myapp-production-service.default.svc.cluster.local:9000

###helm 
https://helm.sh/docs/intro/install/


###install monitoring components using helm

kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring

### debugging 
kubectl patch ds prometheus-prometheus-node-exporter --type "json" -p '[{"op": "remove", "path" : "/spec/template/spec/containers/0/volumeMounts/2/mountPropagation"}]'

### expose svc
kubectl expose service prometheus-grafana --type=NodePort --name=grafana-lb -n monitoring
edit the svc once created to use port 3000
OR
kubectl expose service prometheus-grafana --type=NodePort --name=grafana-lb --port=3000 --target-port=3000 -n monitoring

curl localhost on the above NodePort
Username: admin
Password: prom-operator

### configure service monitoring ### for this to work the app image needs to be updated 
kubectl apply -f example-myapp-production

### configure HPA 
kubectl autoscale deployment myapp-production-deployment --cpu-percent=50 --min=1 --max=5

### generate load 
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "count=0; while sleep 0.01; count=$((count+1)); do wget -q -O- http://myapp-production-service.default.svc.cluster.local:9000; echo "\n"; done"


