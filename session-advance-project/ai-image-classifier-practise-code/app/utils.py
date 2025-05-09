from torchvision import models, transforms
from PIL import Image
import torch
import io
import requests

# Load MobileNet model
def load_model():
    model = models.mobilenet_v2(pretrained=True)
    model.eval()
    return model

# Load labels from ImageNet
def load_labels():
    url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
    labels = requests.get(url).text.strip().split("\n")
    return labels

# Define image transformations
def get_transform():
    return transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

# Preprocess uploaded image file
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    transform = get_transform()
    return transform(image).unsqueeze(0)

