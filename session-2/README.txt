sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
docker-compose build <service_name>
docker-compose up <service_name>
# for the to work we need LB & Auto Port allocation 
docker-compose up -d --scale <service_name>=2
docker run -d -p 80:80 -v /Users/syednadeem/Documents/workspace_dockerK8s_traning/project_sessions/session-2/nginx.conf:/etc/nginx/nginx.conf:ro --name my-nginx nginx:latest


##clean up 
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)