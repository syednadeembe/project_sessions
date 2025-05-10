package main

import (
	"context"
	"fmt"
	"os"
	"path/filepath"

	"k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

func main() {
	userHomeDir, err := os.UserHomeDir()
	if err != nil {
		fmt.Printf("error getting user home dir: %v\n", err)
		os.Exit(1)
	}
	kubeConfigPath := filepath.Join(userHomeDir, ".kube", "config")
	fmt.Printf("Using kubeconfig: %s\n", kubeConfigPath)

	kubeConfig, err := clientcmd.BuildConfigFromFlags("", kubeConfigPath)
	if err != nil {
		fmt.Printf("Error getting kubernetes config: %v\n", err)
		os.Exit(1)
	}

	clientset, err := kubernetes.NewForConfig(kubeConfig)

	if err != nil {
		fmt.Printf("error getting kubernetes config: %v\n", err)
		os.Exit(1)
	}
	// An empty string returns all namespaces
	namespace := "kube-system"
	pods, err := ListPods(namespace, clientset)
	if err != nil {
		fmt.Println(err.Error)
		os.Exit(1)
	}
	for _, pod := range pods.Items {
		fmt.Printf("Pod name: %v\n", pod.Name)
	}
	var message string
	if namespace == "" {
		message = "Total Pods in all namespaces"
	} else {
		message = fmt.Sprintf("Total Pods in namespace `%s`", namespace)
	}
	fmt.Printf("%s %d\n", message, len(pods.Items))

	//ListNamespaces function call returns a list of namespaces in the kubernetes cluster
	namespaces, err := ListNamespaces(clientset)
	if err != nil {
		fmt.Println(err.Error)
		os.Exit(1)
	}
	for _, namespace := range namespaces.Items {
		fmt.Println(namespace.Name)
	}
	fmt.Printf("Total namespaces: %d\n", len(namespaces.Items))
}

func ListPods(namespace string, client kubernetes.Interface) (*v1.PodList, error) {
	fmt.Println("Get Kubernetes Pods")
	pods, err := client.CoreV1().Pods(namespace).List(context.Background(), metav1.ListOptions{})
	if err != nil {
		err = fmt.Errorf("error getting pods: %v\n", err)
		return nil, err
	}
	return pods, nil
}

func ListNamespaces(client kubernetes.Interface) (*v1.NamespaceList, error) {
	fmt.Println("Get Kubernetes Namespaces")
	namespaces, err := client.CoreV1().Namespaces().List(context.Background(), metav1.ListOptions{})
	if err != nil {
		err = fmt.Errorf("error getting namespaces: %v\n", err)
		return nil, err
	}
	return namespaces, nil
}
