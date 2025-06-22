CD : Debuging Session // there are interntial errors in this exercise that we need to fix  
Part 1
# lab setup needs a 3 node cluster setup, I'm using Kind cluster.
https://kind.sigs.k8s.io/docs/user/quick-start/#installation
kind create cluster --name devops-with-syed --config three-node-cluster-setup.yaml
kind get nodes --name devops-with-syed
kubectl run pod1 --image=nginx
kubectl run pod2 --image=nginx
kubectl apply -f svc.yaml
kubectl exec -it pod2 bash
curl myapp.default.svc.cluster.local 
# notice the dns is mapping to pod and firewall is allowing traffic, this is the prime use for core-dns 
kubectl get ep 
# notice the svc and pod are mapped inside endpoints 
kubectl describe po pod1 | grep Node:
# based on "Node" value edit the below command
docker exec -it <Node> bash
iptables -L KUBE-NODEPORTS -t nat
# notice the IP mappings and firewalls, this is the the prime use for kube-proxy

Part 2
kubectl label nodes devops-with-syed-worker dbase=true
# before running the below commands make sure that you have build the images from session-7
kind load docker-image "mongo:latest" --name devops-with-syed
kind load docker-image "syednadeembe/myflaskapp:productionImage_app" --name devops-with-syed
kind load docker-image "syednadeembe/myflaskapp:productionImage_ui" --name devops-with-syed

Exercise 1 : identifying the issues with the deployment from events or deployment 
kubectl apply -f rbac.yaml 
kubectl apply -f dbase.yaml  ### this pod will work be in running state, beacuse of this "kubectl label nodes devops-with-syed-worker dbase=true"
kubectl apply -f app-deployment.yaml ### this pod will not be in running state
kubectl apply -f ui-deployment.yaml ### this pod will be in running state
kubectl get pods 
# one pod will be in pending state 
kubectl label nodes devops-with-syed-worker2 app=true
kubectl get pods ### understand why app pod is crashing 
kubectl label nodes devops-with-syed-worker2 dbase=true
kubectl get pods
# all pods will be in running state

Exercise 2 : apply antiafinity on ui-deployment and see what happness
kubectl scale deployment ui-deployment --replicas=3
kubectl get po -o wide | grep ui-deploy 
# explain why only two replications are running and why is 3rd one in pending state 

Exercise 3 : Affinity & Antiafinity Effect on HPA
kubectl autoscale deployment calculator-app-deployment --cpu-percent=50 --min=2 --max=5
kubectl autoscale deployment ui-deployment --cpu-percent=50 --min=2 --max=5

Exercise 4 : taints and tolerations

kubectl get nodes -o json | jq '.items[].spec.taints'
kubectl apply -f taint-for-master-node.yaml
kubectl apply -f pod-with-master-toleration.yaml
kubectl apply -f taint-for-worker.yml
kubectl apply -f pod-with-worker-toleration.yaml
kubectl apply -f taint-for-worker2.yml
kubectl apply -f pod-with-worker2-toleration.yaml

Exercise 5 : affinity and antiaffinity
kubectl apply -f pod-with-affinity.yaml --> this wont work, understand why
# Rest the cluster or 
kubectl delete -f taint-for-worker.yml
kubectl delete -f taint-for-worker2.yml
kubectl apply -f taint-for-master-node.yaml
kubectl apply -f pod-with-affinity.yaml
kubectl apply -f pods-with-antiaffinity.yaml

Exercise 6 : probs
docker build -t myapp:productionImage_app .
kubectl apply -f probs.yaml --> understand how this works

Exercise 7 : sidecars 
kubectl apply -f sidecar.yaml
