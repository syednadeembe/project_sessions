###############################################################################
Resource Requests:
Purpose: Requests are the amount of resources that the container is guaranteed to receive. Kubernetes will schedule a container on a node only if the node has enough available resources to satisfy the container's resource requests.
Effect: Helps Kubernetes scheduler make intelligent decisions about where to place pods based on available resources.
Impact: If a container exceeds its requests, it may face performance degradation, but it won't be killed by the Kubernetes OOM (Out of Memory) killer.

Resource Limits:
Purpose: Limits are the maximum amount of resources that a container is allowed to use. If a container exceeds its limits, Kubernetes will take action, such as throttling CPU usage or killing the container.
Effect: Prevents a container from consuming excessive resources and impacting other containers on the same node.
Impact: If a container exceeds its limits, Kubernetes may throttle or terminate the container, depending on the resource (CPU or memory) and the container's QoS (Quality of Service) class.

###############################################################################
ConfigMaps and Secrets: 
NOTE: to be discussed only after session 7
Purpose: Seperate application code from configurations

###############################################################################
Liveness Probe:
Purpose: Checks if the container is alive and should be restarted if it's not.
Action: If the liveness probe fails (e.g., the container is unresponsive), Kubernetes restarts the container to try to restore it to a healthy state.
Use case: Use liveness probes to ensure that your application is running correctly within the container.

Readiness Probe:
Purpose: Checks if the container is ready to serve traffic.
Action: If the readiness probe fails, the container is not removed, but it is temporarily removed from the pool of endpoints that serve traffic, and traffic is routed to other containers.
Use case: Use readiness probes to ensure that your application is ready to handle requests before receiving traffic.

###############################################################################
Horizontal Pod Autoscaler (HPA)
NOTE : to be discussed only after session 6
Purpose: Automatically adjust the pod replication on the external load.

###############################################################################
Service Accounts, Role-Based Access Control (RBAC)
NOTE : to be discussed only after session 7
Purpose: Manage Access rules within the cluster resources.

###############################################################################
Ingress Controllers and Ingress Resources
NOTE : to be discussed only after session 5
Ingress Controller:
Purpose: An Ingress controller is a daemon that runs in your cluster and manages incoming traffic to your services. It typically configures a load balancer or a proxy to route traffic to the appropriate services based on rules defined in Ingress resources.
Implementation: There are several Ingress controllers available, such as NGINX Ingress Controller, Traefik, HAProxy Ingress, etc. Each controller implements the Ingress specifications differently.
Features: Ingress controllers can provide features like SSL/TLS termination, path-based routing, and host-based routing.

Ingress Resource:
Purpose: An Ingress resource is a Kubernetes resource that defines how inbound traffic should be routed to services in the cluster. It allows you to configure rules for routing based on paths, hosts, and other criteria.
Configuration: In an Ingress resource, you can specify rules that map requests to services, define TLS settings for secure connections, and set other options like timeouts and load balancing policies.
Usage: Once you create an Ingress resource, the Ingress controller watches for changes to it and configures the external load balancer or proxy accordingly.

###############################################################################
Persistent Volumes (PV) and Persistent Volume Claims (PVC)
NOTE : to be discussed only after session 7
Persistent Volumes (PV):
Purpose: PVs are storage resources in the cluster that have been provisioned by an administrator. They are independent of any pod and exist in the cluster until they are manually deleted.
Storage Types: PVs can be provisioned from different storage classes, which define the type and properties of the underlying storage (e.g., AWS EBS, Azure Disk, NFS).
Access Modes: PVs have access modes (e.g., ReadWriteOnce, ReadOnlyMany, ReadWriteMany) that define how the volume can be mounted by pods.
Lifecycle: PVs have a lifecycle independent of pods. They can be dynamically provisioned or manually created by a cluster administrator.

Persistent Volume Claims (PVC):
Purpose: PVCs are requests for storage by pods. They allow pods to consume storage without needing to know the details of the underlying storage.
Binding: When a PVC is created, the Kubernetes control plane looks for a PV that satisfies the claim's requirements (e.g., storage class, access mode, size). If a suitable PV is found, the PVC is bound to the PV.
Usage: Pods can then use the PVC as a volume in their containers, and Kubernetes will ensure that the pod has access to the requested storage.
Dynamic Provisioning: If no PV is available to satisfy a PVC, some storage classes support dynamic provisioning, where a PV is automatically created to fulfill the claim.

###############################################################################
Taints, Tolerations, Affinity and Anti-affinity
NOTE: need to try this only on cluster setup / kind setup
Taints:
Purpose: Taints are used to repel pods from nodes or to mark nodes for special treatment. They prevent pods from being scheduled onto nodes unless the pods tolerate the taints.
Use Case: Taints are commonly used to reserve nodes for specific workloads or to mark nodes as unsuitable for certain types of pods.

Tolerations:
Purpose: Tolerations are used by pods to tolerate the taints on nodes. Pods with matching tolerations can be scheduled onto nodes with corresponding taints.
Use Case: Tolerations allow pods to be scheduled onto nodes that have specific taints, enabling pods to run on nodes that might otherwise reject them.

Affinity:
Purpose: Affinity is used to influence the scheduling of pods relative to other pods or nodes.
Types:
Node affinity: Specifies rules for pod placement based on node labels.
Pod affinity: Specifies rules for pod placement based on labels of other pods.
Pod anti-affinity: Specifies rules for pod placement to avoid placing pods in the same topology domain (e.g., on the same node or adjacent nodes).
Use Case: Affinity allows you to optimize pod placement based on factors such as node characteristics, workload requirements, and fault tolerance.

Anti-affinity:
Purpose: Anti-affinity is a specific type of affinity that is used to ensure that pods are not co-located with other pods that match certain criteria.
Use Case: Anti-affinity helps improve the availability and fault tolerance of applications by spreading pods across different nodes or zones.

###############################################################################
Kubernetes Jobs and CronJobs
Jobs:
Purpose: Jobs are used to run a task to completion, such as batch processing, data migration, or one-time operations.
Use Cases: Jobs are commonly used for tasks that need to run once or need to be run at a specific time.

CronJobs:
Purpose: CronJobs are used to run tasks on a recurring schedule, similar to cron jobs in a Unix-like system.
Use Cases: CronJobs are useful for tasks that need to be performed regularly, such as backups, log rotation, or periodic maintenance tasks.