### run on local ( Linux follow the below commands for Mac and Windows this wont work )
sudo su -
yum install -y git 
git clone https://github.com/syednadeembe/project_sessions.git
cd project_sessions/session-1
yum install -y python3
yum install python3-pip
pip3 install --no-cache-dir flask flask_restx
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=9000
// Optional : if you get port is already binded error
sudo lsof -i :9000
sudo kill $(lsof -t -i :9000)
flask run --host=0.0.0.0 --port=9000
// Reach to localhost:9000, this should have the webserver running 
### create a virtual environment
python3 -m venv venv

### activate the virtual environment
source venv/bin/activate

### Install the required Flask package
pip3 install --no-cache-dir flask flask_restx
flask run
### this will start the webserver on 127.0.0.1:5000
// Reach to localhost:5000, the webserver will be running but only within local network

curl "http://127.0.0.1:5000/add?num1=5&num2=3" 
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:5000/add
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:5000/add

### Docker Installation 
yum update -y
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user
### to run the application on docker container
docker build -t myflaskapp .
docker run -p 9000:9000 myflaskapp
Now your Flask application should be accessible at http://localhost:9000

####Optional Exercise Only to be done on remote linux server####
###Linux Containers & Namespaces Lab Manual
## Part 1: `runc` Hands-On Lab
### Goal is to Learn how to create a container using `runc` **without Docker**.
---
### 1. **Install Prerequisites**
sudo apt install runc wget tar
# or for RHEL-based systems
sudo yum install runc wget tar
---
### 2. **Prepare Working Directory**
mkdir -p ~/runc-container/rootfs
cd ~/runc-container
---
### 3. **Download and Extract Alpine Root Filesystem**
cd rootfs
wget https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-minirootfs-3.21.3-x86_64.tar.gz
sudo tar -xzf alpine-minirootfs-3.21.3-x86_64.tar.gz
cd ..
---
### 4. **Generate OCI Runtime Spec**
runc spec
---
### 5. **Edit `config.json`**
- Set `"terminal": true`
- Change:
  ```json
  "args": ["/bin/sh"]
  ```
---
### 6. **Run the Container**
sudo runc run mycontainer
##Inside the container:
hostname
ls /
exit
---
### 7. **(Optional) Use Create + Start Mode**
sudo runc create mycontainer
sudo runc start mycontainer
##Use `runc exec` to interact:
sudo runc exec -t mycontainer /bin/sh
---
### 8. **Cleanup**
sudo runc kill mycontainer SIGKILL
sudo runc delete mycontainer
---
## Part 2: Linux Namespaces Lab
### Understand how different Linux namespaces isolate system resources.
---
### Exercises
### 1. **UTS Namespace (hostname isolation)**
sudo unshare --uts bash
hostname container1
hostname
exit
---
### 2. **PID Namespace (process tree isolation)**
sudo unshare --pid --fork --mount-proc bash
ps aux
exit
---
### 3. **Network Namespace (network stack isolation)**
sudo unshare --net bash
ip link
ip link set lo up
ping 127.0.0.1
ping google.com    # will fail
exit
---
### 4. **Combined Isolation (simulate container)**
sudo unshare --uts --ipc --net --pid --fork --mount-proc bash
hostname mycontainer
ip link
ps aux
exit
---
###  Restore Hostname if Changed
sudo hostnamectl set-hostname ip-10-0-13-212
