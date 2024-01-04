This is a DevOps Project Road Map, that takes a simple source code and implements the most common DevOps iterations to it.
Find Details about the project here: https://www.devopswithsyed.com and https://www.linkedin.com/feed/update/urn:li:activity:7122220432383967233/
![image](https://github.com/syednadeembe/project_sessions/assets/29227348/203370cc-e093-4fb0-b3d4-dfc741715613)

# [Session 0: Environment setup](https://github.com/syednadeembe/project_sessions/tree/main/session-0)
**Project:** Requirement Details, what is that is needed from the team. We will draw the blueprint of the iterations/Agile based development approach. 
Parallelly a local setup as well as remote a setup will be done for Kubernetes cluster.

**Project:** Installing and understanding architecture for Docker, Kubernetes, Jenkins, and setting up remote git repo and remote working server in AWS.
# [Session 1: Creating the Base Image](https://github.com/syednadeembe/project_sessions/tree/main/session-1)
**Project:** Students will Dockerize a simple web application, such as a Flask or Node.js app.
They will create a Dockerfile to build the application image and run it as a container.
The project will include steps to test the container locally and ensure it functions as expected.

# [Session 2: Docker Compose and Multi-Stage Builds](https://github.com/syednadeembe/project_sessions/tree/main/session-2)
**Project:** Containerizing a Microservices Architecture
Students will containerize a microservices-based application using Docker Compose.
They will define multiple services for each microservice and establish communication between them.
The project will involve creating a Docker Compose YAML file and running the application locally using Docker Compose.

# [Session 3: Introduction to Kubernetes](https://github.com/syednadeembe/project_sessions/tree/main/session-3)
**Project:** Setting Up a Local Kubernetes Cluster
Students will use the Kubernetes cluster, they will deploy and manage sample applications and verify its successful deployment and functioning on the cluster.
The project will focus on understanding the Kubernetes architecture and using kubectl commands for cluster management.

# [Session 4: Deploying Microservices with Kubernetes](https://github.com/syednadeembe/project_sessions/tree/main/session-4)
**Project:** Deploying Microservices on Kubernetes
Students will containerize multiple microservices and create Kubernetes deployment manifests for each service.
They will define a Kubernetes service to enable communication between microservices.
The project will involve deploying the microservices on a Kubernetes cluster and testing their interaction and scalability.

# [Session 5: Kubernetes Networking and Service Discovery](https://github.com/syednadeembe/project_sessions/tree/main/session-5)
**Project:** Implementing Ingress and Load Balancing
Students will configure an Ingress controller and define rules for routing traffic to different microservices.
They will set up load balancing and test the routing of requests between services.
The project will demonstrate how to expose services to the outside world and enable service discovery within the Kubernetes cluster.

# [Session 6: Monitoring, Logging, Pipelines and Scaling](https://github.com/syednadeembe/project_sessions/tree/main/session-6)
**Project:** Implementing Monitoring Scaling and Pipelines 
Students will configure monitoring using Prometheus and Grafana to collect and visualize metrics from their Kubernetes cluster.
They will set up a CI/CD pipeline using a tool like GitLab/Jenkins CI/CD to automate the deployment of their application on Kubernetes.
The project will emphasize best practices for logging, monitoring, and continuous deployment in a Kubernetes environment. We will also spend time in setting up metric-server and HPA.

# [Session-ui](https://github.com/syednadeembe/project_sessions/tree/main/session-ui) [& Session-dbase:](https://github.com/syednadeembe/project_sessions/tree/main/session-dbase) [Adding UI and Mongo Database to the Project]()
**Project:** We will be creating the required UI layer and Database layer to the project.
The Network will be configured for these layers and the integration for the 3-tier architecture will be set. The application code will also need to be changed to make the integration work. We will be setting up the environment with docker-compose first and then with Kubernetes deployments.

# [Session 7: 3-tier architecture deployment with UI, Application and Database components](https://github.com/syednadeembe/project_sessions/tree/main/session-7)
**Project:** We will first do session-ui and session-backend to separately understand the components and their network. All the components will be first deployed as isolated docker components and then we will put everything in as a release and manage it via release charts.
Dry run and state session management will be checked. Component Network will be configured and End-point mapping will be set. RBAC's and Service accounts will be implemented within the project to implement component-level security.

# [Debug Session]()
**Project:** We will inject a fault into the setup created in last 7 sessions and see what are the best and proper isolation techniques. We will be isolating application issues, container issues, cluster issues, and network issues from one another. 
