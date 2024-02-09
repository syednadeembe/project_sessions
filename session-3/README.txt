sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# part-1
# understand how docker networking and scaling works
# understand the user of docker-compose and multi-stage build wrt management and security
cd part-1
docker-compose build
docker-compose up -d 
docker-compose ps
docker-compose up -d --scale <service_name>=2 

#part-2
# understand how one has to create a self managed load balancer in docker
docker-compose build <service_name>
docker-compose up <service_name>

##clean up 
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
