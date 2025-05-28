package main

import (
    "bufio"
    "context"
    "fmt"
    "os"
    "path/filepath"

    "github.com/spf13/cobra"
    "k8s.io/api/core/v1"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
)

// Global variable for the Kubernetes clientset
var clientset *kubernetes.Clientset
var image string // Image flag for the run command

// Root command
var rootCmd = &cobra.Command{
    Use:   "get_all_pods",
    Short: "A CLI tool to interact with Kubernetes pods",
}

// List command to list pods in a namespace
var listCmd = &cobra.Command{
    Use:   "list [namespace]",
    Short: "List pods in the given namespace",
    Args:  cobra.ExactArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
        namespace := args[0]
        pods, err := ListPods(namespace, clientset)
        if err != nil {
            fmt.Println("Error listing pods:", err)
            os.Exit(1)
        }
        for _, pod := range pods.Items {
            fmt.Printf("Pod name: %v\n", pod.Name)
        }
    },
}

// Run command to create a pod
var runCmd = &cobra.Command{
    Use:   "run [pod-name]",
    Short: "Create a pod in the given namespace with a specified image",
    Args:  cobra.ExactArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
        podName := args[0]
        namespace := promptForNamespace()

        if image == "" {
            image = "k8s.gcr.io/pause:3.1" // default image
        }

        err := CreatePod(namespace, podName, image, clientset)
        if err != nil {
            fmt.Println("Error creating pod:", err)
            os.Exit(1)
        }
    },
}

func init() {
    // Set up the kubeconfig and clientset
    userHomeDir, err := os.UserHomeDir()
    if err != nil {
        fmt.Printf("Error getting user home dir: %v\n", err)
        os.Exit(1)
    }
    kubeConfigPath := filepath.Join(userHomeDir, ".kube", "config")
    kubeConfig, err := clientcmd.BuildConfigFromFlags("", kubeConfigPath)
    if err != nil {
        fmt.Printf("Error getting kubernetes config: %v\n", err)
        os.Exit(1)
    }
    clientset, err = kubernetes.NewForConfig(kubeConfig)
    if err != nil {
        fmt.Printf("Error creating kubernetes clientset: %v\n", err)
        os.Exit(1)
    }

    // Add image flag to the run command
    runCmd.Flags().StringVarP(&image, "image", "i", "", "Container image to use (default is 'k8s.gcr.io/pause:3.1')")

    // Add subcommands to the root command
    rootCmd.AddCommand(listCmd)
    rootCmd.AddCommand(runCmd)
}

// ListPods function to get a list of pods in a namespace
func ListPods(namespace string, client kubernetes.Interface) (*v1.PodList, error) {
    pods, err := client.CoreV1().Pods(namespace).List(context.Background(), metav1.ListOptions{})
    if err != nil {
        return nil, fmt.Errorf("error getting pods: %v", err)
    }
    return pods, nil
}

// CreatePod function to create a pod
func CreatePod(namespace string, podName string, image string, client kubernetes.Interface) error {
    pod := &v1.Pod{
        ObjectMeta: metav1.ObjectMeta{
            Name: podName,
        },
        Spec: v1.PodSpec{
            Containers: []v1.Container{
                {
                    Name:  "main",
                    Image: image,
                },
            },
        },
    }
    _, err := client.CoreV1().Pods(namespace).Create(context.Background(), pod, metav1.CreateOptions{})
    if err != nil {
        return fmt.Errorf("failed to create pod: %v", err)
    }
    fmt.Printf("Pod '%s' created successfully in namespace '%s' with image '%s'\n", podName, namespace, image)
    return nil
}

// Prompt for user input (pod name)
func promptForInput(prompt string) string {
    fmt.Print(prompt)
    reader := bufio.NewReader(os.Stdin)
    input, err := reader.ReadString('\n')
    if err != nil {
        fmt.Println("Error reading input:", err)
        os.Exit(1)
    }
    return input[:len(input)-1]
}

// Prompt for namespace, defaulting to "default" if empty
func promptForNamespace() string {
    namespace := promptForInput("Enter the namespace for the pod (default is 'default'): ")
    if namespace == "" {
        namespace = "default"
    }
    return namespace
}

func main() {
    if err := rootCmd.Execute(); err != nil {
        fmt.Println("Error executing command:", err)
        os.Exit(1)
    }
}
