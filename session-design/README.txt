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
kind load docker-image "myapp:productionImage_app" --name devops-with-syed
kind load docker-image "myapp:productionImage_ui" --name devops-with-syed

Exercise 1 : identifying the issues with the deployment from events or deployment 
kubectl apply -f rbac.yaml 
kubectl apply -f dbase.yaml  ### this pod will be in running state
kubectl apply -f app-deployment.yaml 
kubectl apply -f ui-deployment.yaml
kubectl get pods 
# one pod will be in pending state 
kubectl label nodes devops-with-syed-worker2 app=true
kubectl get pods
# all pods will be in running state

Exercise 2 : apply HPA on App deployment and see what happness, with max limit as 5
# for HPA reference see session-6 content

Exercise 3 : apply antiafinity on ui-deployment and see what happness
kubectl scale deployment ui-deployment --replicas=3
kubectl get po -o wide | grep ui-deploy 
# explain why only two replications are running and why is 3rd one in pending state 

Exercise 4 : apply HPA on ui-deployment and see what happness, with max limit as 5
# for HPA reference see session-6 content
<<<<<<< HEAD

Clean Up: kind delete cluster --name devops-with-syed
=======
>>>>>>> bec79ca47588054051ed353881a4195baa989b81
