from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils import load_model, load_labels, preprocess_image
import torch

app = FastAPI()

model = load_model()
labels = load_labels()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img_tensor = preprocess_image(contents)

    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
        label = labels[predicted.item()]

    return JSONResponse({"class": label})

