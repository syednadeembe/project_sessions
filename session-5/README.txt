###deploy both base as well as the production deployments
kubectl apply -f myapp-production-deployment.yaml
kubectl apply -f myapp-base-deployment.yaml

###validate pods, deployments, svc and endpoints
kubectl get pods
kubectl get svc 
kubectl get deployment
kubectl get endpoints

### Under Service Discovery 
<dont only on labsetup 
- edit the configmap of coredns to add logs and debug sections and then rollout
kubectl -n kube-system rollout restart deployment coredns >
### What enables a pod to find and communicate with each other without hardcoding IP 
- CoreDNS : maps service names to IPs
- Headless Services : no cluster IP, returns pod IPs instead
- External Name : maps service to an external DNS name

### DNS-Based Service Discovery (ClusterIP)
kubectl run web --image=nginx --restart=Never --port=80
kubectl expose pod web --port=80 --target-port=80 --name=web-service

kubectl run test --image=busybox --rm -it --restart=Never -- /bin/sh
# Inside the test pod
wget -qO- http://web-service

### Role of kube-proxy
kubectl get svc myapp-production-clusterip
sudo iptables-save | grep <ClusterIP of any Service>
sudo iptables -t nat -L KUBE-SERVICES -n | grep <cluster-ip>
sudo iptables -t nat -L KUBE-SERVICES -n --line-numbers

## For Example #######################################

sudo iptables-save | grep 10.104.12.212
- You’ll see something like: -A KUBE-SERVICES -d 10.104.12.212/32 -p tcp --dport 80 -j KUBE-SVC-ABCD1234
- Note down the service chain ID: KUBE-SVC-ABCD1234
sudo iptables-save | grep KUBE-SVC-ABCD1234
- You will get endpoint chains (each represents a Pod)

Service ClusterIP (10.104.12.212:9000)
    ⇓
iptables KUBE-SERVICES
    ⇓
KUBE-SVC-YGPY7WI7YZ3DB7GT
    ⇓
KUBE-SEP-XYZ → Pod IP:Port (e.g., 10.244.1.25:9000)
####################################################

### For Headless Service
kubectl apply -f headless.yaml
kubectl run testpod --image=busybox:1.28 -it --rm -- /bin/sh
ping db-0.headless-db
ping db-1.headless-db

### For External Service
kubectl apply -f external_service.yaml
kubectl run curlpod --image=radial/busyboxplus:curl -it --rm
# Inside the pod
nslookup external-google.default.svc.cluster.local

###download the ingress ngix-controller 
curl -LO https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.1/deploy/static/provider/baremetal/deploy.yaml
kubectl apply -f deploy.yaml

###read more about the controller here
https://kubernetes.github.io/ingress-nginx/deploy/

###apply the ingress-controller-objects
kubectl apply -f ingress-controller-objects.yaml

###describe to see results ingress object 
kubectl describe ingress myapp-ingress
### validate the rules 
  myapp.local
               /base         myapp-base-service:9000 (10.1.2.24:9000,10.1.2.25:9000)
               /production   myapp-production-service:9000 (10.1.2.26:9000,10.1.2.27:9000)


###navigate to ingress-nginx and check the controller logs 
kubectl logs -f deployment/ingress-nginx-controller -n ingress-nginx

###open another terminal 

###get the ingress-nginx controller IP 
kubectl get svc -n ingress-nginx | grep -e "ingress-nginx-controller"

###Run a dummy pod for validation
kubectl run nginx --image=nginx
kubectl exec -it nginx bash
echo "<ingress-nginx-controller-IP>       myapp.local" >> /etc/hosts
echo "10.99.132.189       myapp.local" >> /etc/hosts
curl myapp.local/base
curl myapp.local/production

###again check controller logs 
kubectl logs -f deployment/ingress-nginx-controller
