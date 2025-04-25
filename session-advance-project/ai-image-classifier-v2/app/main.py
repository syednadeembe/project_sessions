from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils import load_model, load_labels, preprocess_image
import torch

app = FastAPI()

# Serve HTML templates
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

model = load_model()
labels = load_labels()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img_tensor = preprocess_image(contents)

    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
        label = labels[predicted.item()]

    return JSONResponse({"class": label})
