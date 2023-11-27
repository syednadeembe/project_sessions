### these tests should be part of the CI pipelines and can also be executed manually

### the webserver should be running on localhost:9000
curl "http://127.0.0.1:9000/add?num1=5&num2=3" 
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:5000/add
curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 3}' http://127.0.0.1:5000/add


### to run the application on docker container
docker build -t ../session-1/myflaskapp .
docker run -p 9000:9000 myflaskapp
Now your Flask application should be accessible at http://localhost:9000

### include api_test.sh as a stage in your CI pipeline