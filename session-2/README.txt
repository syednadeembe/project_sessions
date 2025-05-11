WhiteBoard Content
This session starts with container runtime ( low-level and hight-level flow) in the batch
Then we discuss Dockerfile and Dockerfile commands ( only what we are using at the moment )


Lab Content - Docker networking
### run the application on docker container (terminal-1)
docker build -t myflaskapp .
docker run -p 9000:9000 myflaskapp
### your Flask application should be accessible at http://localhost:9000

### test it in another teminal (terminal-2)
curl "http://127.0.0.1:9000/add?num1=5&num2=3" 
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:9000/add
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:9000/add

### create and understand dockerfile
### open another teminal (terminal-3)
mkdir nginx
cd nginx
echo "From nginx" >> Dockerfile
docker build -t mynginx . 
docker run -p 80:80 mynginx

### test networking in (terminal-2)
mynginxID=`docker ps | grep mynginx | awk '{print $1}'`
myflaskID=`docker ps | grep myflaskapp | awk '{print $1}'`
docker inspect $mynginxID | grep IPAddress
docker inspect $myflaskID | grep IPAddress

### login to the nginx pod and curl the application server on the IP ---> this will work
### login to the nginx pod and curl the application server on the hostname ---> this wont work
### we need to understand how docker gateway works and how networking is working

### how to create dedicated docker network for the containers and understand Docker's built-in DNS service and gateway
### stop all running containers from this Lab

docker network create appnetwork
docker run -p 9000:9000 --hostname myapp --name myapp --network appnetwork myflaskapp &
docker run -it --rm -p 80:80 --network appnetwork mynginx bash
### login to the nginx pod and curl the application server on the hostname ---> this will work
### hostname of our app is myapp
cat /etc/resolv.conf

Lab Content - Docker storage
docker run -it --rm -p 80:80 --network appnetwork mynginx bash
cd /opt
mkdir testfolder
cd testfolder
echo "container-1 updates" >> logs.txt
### exit the container and re-run mynginx container ---> logs.txt and the folder will be deleted

### how to create dedicated docker volume for the containers also explain NFS concept 
### (terminal-1)
docker volume create nginx-volume 
docker run -it --rm -p 80:80 -v nginx-volume:/opt/testfolder --network appnetwork mynginx bash
cd /opt
mkdir testfolder
cd testfolder
echo "container-1 updates" >> logs.txt

### (terminal-2)
docker run -it --rm -p 81:80 -v nginx-volume:/opt/testfolder --network appnetwork mynginx bash
cd /opt/testfolder
cat logs.txt


