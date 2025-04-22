
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import product

app = FastAPI(title="Inventory Management App for E-Commerce")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router, prefix="/api/products")
