from kubernetes import client, config

def list_pods(namespace):
    # Set the Kubernetes configuration to use the proxy exposed at localhost:8001
    configuration = client.Configuration()
    configuration.host = "http://localhost:8001"

    # Load the Kubernetes configuration
    client.Configuration.set_default(configuration)

    # Create a Kubernetes API client
    v1 = client.CoreV1Api()

    # Get the list of pods in the specified namespace
    pods = v1.list_namespaced_pod(namespace)

    # Extract and print the names of all pods
    for pod in pods.items:
        print(pod.metadata.name)

if __name__ == "__main__":
    # Customize the value here based on your desired namespace
    namespace = "default"

    list_pods(namespace)

