### setting up remote jenkins server for CI
sudo yum update –y
sudo wget -O /etc/yum.repos.d/jenkins.repo     https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo yum upgrade
sudo dnf install java-17-amazon-corretto -y
sudo mount -o remount,size=5G /tmp/
sudo yum install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker jenkins
sudo yum install git -y
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
### switch the user from root to jenkins and try to run docker command
sudo su -s /bin/bash jenkins 
whoami
docker ps 
cd ~
git clone https://github.com/syednadeembe/project_sessions.git
cd session-1
docker build -t myflaskapp .
docker run -p 9000:9000 myflaskapp &
### application should come up and delete the container after testing 
### jenkins job creation 
Jenkins Job Creation UI 
### create the application build job
### go to Build Steps and select the Execute shell 
### write the following in Execute shell:
rm -rf project_sessions
git clone https://github.com/syednadeembe/project_sessions.git
cd project_sessions/session-1
docker build -t myflaskapp .
### save and run the build job 
### this job will create the docker image on the machine. Login to the machin and verify that the docker image is created 
### if you have a git hub account then you can also add the following command to the pipeline to push the image to that account, this is how the execute shell will look like:
rm -rf project_sessions
git clone https://github.com/syednadeembe/project_sessions.git
cd project_sessions/session-1
docker build -t myflaskapp:v1 .
docker tag myflaskapp:v1 <your_repo_name>
docker push <your_repo_name>




