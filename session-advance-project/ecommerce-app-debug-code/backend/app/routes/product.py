from fastapi import APIRouter
from app.models import Product
from app.db import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products():
    db = get_db()
    products = list(db.products.find())
    return products

@router.post("/", response_model=Product)
def add_product(product: Product):
    db = get_db()
    db.products.insert_one(product.dict())
    return product
