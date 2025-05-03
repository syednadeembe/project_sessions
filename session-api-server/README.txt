############################## do this after session-0 #################################

### connecting via kubectl, to make this work you need to have a kubeconfig file
### connecting via curl, to make this work you need to have the token or certs
### connecting via client, to make this work you need to have either token or kubeconfig

################################ connecting via kubectl ################################
https://kubernetes.io/docs/reference/kubectl/
https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/

################################ connecting via curl ###################################
### Step to access via curl with certs
cd session-api-server
kubectl apply -f curl_code
cat  /Users/syednadeem/.kube/config |grep client-certificate-data | awk -F ' ' '{print $2}' |base64 -d > client-cert.pem
cat  /Users/syednadeem/.kube/config |grep client-key-data | awk -F ' ' '{print $2}' |base64 -d > client-key.pem
APISERVER=`cat  /Users/syednadeem/.kube/config |grep server | awk -F ' ' '{print $2}'`
echo $APISERVER
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods
curl --cert client-cert.pem --key client-key.pem -k $APISERVER/api/v1/namespaces/default/pods | jq -r '.items[].metadata.name'

### Steps to access via curl with token
TOKEN=`kubectl get secret  my-service-account-token -o jsonpath='{.data.token}' | base64 --decode`
echo $TOKEN
curl -k $APISERVER/api/v1/namespaces/default/pods --header "Authorization: Bearer $TOKEN"

### Make use of kubectl proxy
kubectl proxy
curl -s http://localhost:8001/api/v1/namespaces | jq -r '.items[].metadata.name'
curl -X POST -H "Content-Type: application/json" -d '{"apiVersion":"v1","kind":"Namespace","metadata":{"name":"new-namespace"}}' http://localhost:8001/api/v1/namespaces

curl -X DELETE http://localhost:8001/api/v1/namespaces/new-namespace

curl -s http://localhost:8001/api/v1/namespaces/default/pods | jq -r '.items[].metadata.name'

cat <<EOF | curl -s http://localhost:8001/api/v1/namespaces/default/pods --data @- -H "Content-Type: application/json"
{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "busybox-pod"
  },
  "spec": {
    "containers": [
      {
        "name": "busybox-container",
        "image": "busybox",
        "command": ["sleep", "3600"]
      }
    ]
  }
}
EOF

curl -X DELETE http://localhost:8001/api/v1/namespaces/default/pods/busybox-pod

################################ connecting via client ###################################

### For python_code we need to have required bundles installed in the server
### Make sure python3 is installed on the server
cd session-api-server/python_code

### Depending upon the operating system the below commands will change
### Following is what works on mac and linux 
python3 -m venv venv
source venv/bin/activate
pip install kubernetes
### The above command just activate a virtual environment and now you can run the below command 
python3 list_pods.py
### Deactivate the virtaul environment once done with the below command 
deactivate

### For go_code you can run the code or create an executable and then run the executable from anywhere
### However you need to have go installed
cd session-api-server/go_code
go mod init get_pods
go mod tidy
go run main.go
go build  -o get_all_pods
