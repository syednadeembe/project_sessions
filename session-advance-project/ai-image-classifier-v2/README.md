# AI Image Classifier

This project is a lightweight AI-based image classifier built using FastAPI and MobileNetV2. It allows users to upload an image and receive a predicted class label based on the ImageNet dataset.

## Features

- **FastAPI Backend**: A modern web framework for building APIs with Python.
- **MobileNetV2 Model**: A pre-trained lightweight deep learning model optimized for mobile and edge devices.
- **Interactive Web Interface**: Upload images directly via a user-friendly web page.
- **REST API**: Easily integrate the classifier into other applications using the provided API endpoint.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Python 3.11](https://www.python.org/downloads/)

---

### Installation

Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-image-classifier-v2
   docker build -t ai-image-classifier .
   docker run -p 8000:8000 ai-image-classifier
##Access the application at http://localhost:8000.

Example Request
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/image.jpg"

Example Response
{
  "class": "golden retriever"
}

ai-image-classifier-v2/
├── app/
│   ├── [main.py](http://_vscodecontentref_/1)          # FastAPI application
│   ├── [utils.py](http://_vscodecontentref_/2)         # Utility functions for model and image processing
│   ├── templates/       # HTML templates
│   └── static/          # Static files (CSS, JS, etc.)
├── k8s/                 # Kubernetes deployment files
├── test_data/           # Sample images for testing
├── Dockerfile           # Docker configuration
├── [requirements.txt](http://_vscodecontentref_/3)     # Python dependencies
└── [README.md](http://_vscodecontentref_/4)            # Project documentation

Deployment With Kubernetes
Update the k8s/deployment.yaml file with your Docker Hub username:
image: your-dockerhub-username/ai-image-classifier:latest
Apply the Kubernetes manifests: kubectl apply -f k8s/
Access the application via the configured ingress host.

Acknowledgments
PyTorch
FastAPI
MobileNetV2