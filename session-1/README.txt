### create a virtual environment
python3 -m venv venv

### activate the virtual environment
source venv/bin/activate

### Install the required Flask package
pip3 install --no-cache-dir flask flask_restx
flask run

### this will start the webserver on 127.0.0.1:5000
curl "http://127.0.0.1:5000/add?num1=5&num2=3" 
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:5000/add
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:5000/add


### to run the application on docker container
docker build -t myflaskapp .
docker run -p 9000:9000 myflaskapp
Now your Flask application should be accessible at http://localhost:9000
