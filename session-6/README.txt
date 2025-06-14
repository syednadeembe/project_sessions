######################################################################################
# Setup 
######################################################################################
### Before running deployment make sure the images are persent in the system, use updated-image-with-metrics for building.
### deploy the production deployments
kubectl apply -f example-myapp-production/deployment.yaml

### deploy the production deployments svc
kubectl apply -f example-myapp-production/svc.yaml

### create nginx for testing
kubectl run nginx --image=nginx

### curl the myapp-production service from nginx prod
kubectl exec -it nginx bash
curl myapp-production-service.default.svc.cluster.local:80

######################################################################################
# HPA
######################################################################################

### Before running HPA, metrics server should be installed if not present by default in your cluster
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
  # if READY value is 0/1 for deployment.apps/metrics-server after running  below command 
  # kubectl get deploy -n kube-system
  # then do following as per https://dev.to/docker/enable-kubernetes-metrics-server-on-docker-desktop-5434
    # wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    # add below arg at Deployment->spec->template->spec->args
    # --kubelet-insecure-tls

kubectl -n kube-system patch deployment metrics-server \
  --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
    
### configure HPA 
kubectl autoscale deployment myapp-production-deployment --cpu-percent=50 --min=1 --max=5

### generate load 
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "count=0; while sleep 0.01; count=$((count+1)); do wget -q -O- http://myapp-production-service.default.svc.cluster.local:80; echo "\n"; done"

### generate extra load 
kubectl run -i --tty load-generator --rm \
  --image=busybox:1.28 --restart=Never \
  -- /bin/sh -c 'count=0; while true; do for i in $(seq 1 20); do wget -q -O- http://myapp-production-service.default.svc.cluster.local:80 >/dev/null & done; wait; count=$((count+1)); echo "Batch $count sent"; done'


######################################################################################
# VPA
######################################################################################
### Setting up VPA needs manual installtion as VPA is not supported out of the box like HPA 
### Following github project is where the VPA operator is managed : https://github.com/kubernetes/autoscaler
cd project_sessions/session-6/vpa
kubectl api-resources | grep hpa ---> hpa api is present by default
kubectl api-resources | grep vpa ---> vpa api is not present by default
git clone https://github.com/kubernetes/autoscaler.git
cd autoscaler/vertical-pod-autoscaler/
./hack/vpa-up.sh
kubectl api-resources | grep vpa ---> notice the k8s newly added api-resources 
kubectl explain  verticalpodautoscalers --recursive | less
kubectl explain  verticalpodautoscalercheckpoints --recursive | less
### verify metrics server is running 
cd ../..
kubectl top pods
kubectl apply -f vpa.yaml
kubectl apply -f load-generator.yaml
kubectl get vpa -w


######################################################################################
# Monitoring
######################################################################################
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
kubectl expose service prometheus-grafana --type=NodePort --name=grafana-lb --port=3000 --target-port=3000 -n monitoring
kubectl expose service prometheus-kube-prometheus-prometheus --type=NodePort --name=prometheus-lb  -n monitoring

### curl localhost on the above NodePorts
Username: admin
Password: prom-operator 
OR 
Username: admin
Password: admin

### configure service monitoring ### for this to work the app image needs to be updated 
kubectl apply -f example-myapp-production

### customise promethus to only see your smon / endpoints, update this in the promethus object :
kubectl edit prom prometheus-kube-prometheus-prometheus -n monitoring 
### replace the following code 
  serviceMonitorNamespaceSelector: {}
  serviceMonitorSelector:
    matchLabels:
      release: prometheus
### with the below section 
  serviceMonitorNamespaceSelector:
    matchLabels:
      kubernetes.io/metadata.name: default
  serviceMonitorSelector: {}
### restart the prometheus-kube-prometheus-operator pod by deleting 
### login to prometheus UI portails --> Status --> Targets 
Re-Run the Load testing from HPA section 
### revert the prom object back for Graphana to work once your are done.

### Loki add on 

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install loki-stack grafana/loki-stack \
  --namespace monitoring \
  --create-namespace \
  --set promtail.enabled=true

Loki service available as: http://loki-stack.monitoring.svc.cluster.local:3100

### test graphana and loki connectivity 
kubectl exec -it <grafana-pod> -n monitoring -- sh
/usr/share/grafana $ curl http://loki-stack.monitoring.svc.cluster.local:3100/ready
ready

### port forward with 
kubectl port-forward svc/grafana-lb 3000:3000 -n monitoring

### register as loki in graphana 
kubectl exec -it <grafana-pod> -n monitoring -- sh
curl -X POST http://localhost:3000/api/datasources \
  -H "Content-Type: application/json" \
  -u admin:prom-operator \
  -d '{
    "name":"Loki",
    "type":"loki",
    "access":"proxy",
    "url":"http://loki-stack.monitoring.svc.cluster.local:3100",
    "basicAuth": false,
    "isDefault": false
}'

### Navigate to Graphana UI --> Explore --> Outline should show Loki

### To make Loki fetch all namespace we need a over ride for helm
create promtail-values.yaml
###########################
promtail:
  enabled: true
  config:
    snippets:
      extraScrapeConfigs: |
        - job_name: kubernetes-pods
          pipeline_stages:
            - cri: {}
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - action: replace
              source_labels: [__meta_kubernetes_pod_node_name]
              target_label: node_name
            - action: replace
              source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
            - action: replace
              source_labels: [__meta_kubernetes_pod_name]
              target_label: pod
            - action: replace
              source_labels: [__meta_kubernetes_pod_container_name]
              target_label: container
            - action: replace
              replacement: /var/log/pods/*/*/*.log
              target_label: __path__
###########################
helm upgrade --install loki-stack grafana/loki-stack \
  --namespace monitoring \
  -f promtail-values.yaml

kubectl rollout restart daemonset loki-stack-promtail -n monitoring
kubectl logs -n monitoring -l app.kubernetes.io/name=promtail

  


