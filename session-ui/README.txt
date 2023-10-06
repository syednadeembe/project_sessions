## Pre-requist 
1. kubectl apply -f deployment.yaml // use docker-compose build from session-2 for image creation 
2. kubectl port-forward service/myapp-production-service 8443:web // Expose the service for the js file on http://localhost:8443/
3. docker build -t calculator-ui:latest -f Dockerfile .
4. docker run -d -p 8080:80 calculator-ui:latest
5. navigate to http://localhost:8080/ for the UI
