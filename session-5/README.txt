###deploy both base as well as the production deployments
kubectl apply -f myapp-production-deployment.yaml
kubectl apply -f myapp-base-deployment.yaml

###validate pods, deployments, svc and endpoints
kubectl get pods
kubectl get svc 
kubectl get deployment
kubectl get endpoints

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
