sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

###  part-1 white board
# understand how docker networking and scaling works from the last session and corelate 
# understand the user of docker-compose and multi-stage build wrt management and security
cd part-1
docker build -t myflaskapp -f Dockerfile.base .
# try to create multiple replication for HA
#( terminal-1 )
docker run -p 9000:9000  --name myapp-1 myflaskapp
#( terminal-2 )
docker run -p 9000:9000  --name myapp-2 myflaskapp---> this command will fail
docker rm myapp-2
docker run -p 9001:9000  --name myapp-2 myflaskapp
# port management devops resposibility 
# security is devops resposibility 
# scaling is devops resposibility 
# load-balancing is devops resposibility
# service discovery is devops resposibility 
# orchestration of application microservices ( UI, APP, DBase ) ( network ) etc, is user resposibility
#( terminal-3 )
docker stop myapp-1 myapp-2
docker rm myapp-1 myapp-2
# you should be in folder : part-1 
docker-compose build
docker-compose up -d 
docker-compose ps
docker-compose up -d --scale nginx=2 ---> this command will fail
docker-compose down
cd ../part-2
docker-compose build 
docker-compose up 

#### part-2 white board 
# understand multistage build
# understand how one has to create a self managed load balancer 
##clean up 
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)

#### part-3 white board for github actions 
# enable workflows and explain CI and stages that need to be part of CI
