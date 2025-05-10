from fastapi import FastAPI
from app.routes import product

app = FastAPI()

app.include_router(product.router, prefix="/api/products", tags=["products"])

@app.get("/")
def root():
    return {"message": "E-commerce API is running"}
