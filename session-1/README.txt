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


### to run the application on docker container
docker build -t myflaskapp .
docker run -p 9000:9000 myflaskapp
Now your Flask application should be accessible at http://localhost:9000
