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


Tested in Rocky Linux 9.5
# 1. Remove old version (optional but clean)
sudo dnf remove golang -y

# 2. Download and install latest Go manually (1.24.1 as of now)
cd /usr/local
sudo curl -OL https://go.dev/dl/go1.24.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.24.1.linux-amd64.tar.gz
sudo rm -f go1.24.1.linux-amd64.tar.gz

# 3. Set PATH (permanently by editing /etc/profile.d/go.sh or ~/.bashrc)
export PATH=/usr/local/go/bin:$PATH

# 4. Verify
go version
cd session-api-server/go_code
go mod init get_pods
go mod tidy
go run main.go
go build  -o get_all_pods


# GoLang client-go to access Kubernetes 

Running binary from Remote Client Linux Machine
Copy binary (get_all_pods) and .kube/config file to  Client Linux Machine
scp -P 2222 root@localhost:/root/project_sessions/session-api-server/go_code/get_all_pods .
scp -v -P 2222 root@localhost:/root/.kube/config .

./get_all_pods

Example Usage

# Using default image (pause)
./get_all_pods run test-pod

# Using custom image (nginx)
./get_all_pods run my-nginx-pod --image nginx:latest

# Using short flag for image
./get_all_pods run alpine-pod -i alpine

# List pods in the 'default' namespace
./get_all_pods list default

# List pods in the 'test-ns' namespace
./get_all_pods list test-ns