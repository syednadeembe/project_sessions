from fastapi import APIRouter, HTTPException
from app.models import Product, ProductIn
from app.db import get_db
from typing import List
from bson import ObjectId

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products():
    db = get_db()
    products = list(db.products.find())
    return [
        {
            "id": str(p["_id"]),
            "name": p["name"],
            "price": p["price"],
            "category": p.get("category", ""),
            "description": p.get("description", ""),
            "stock": p.get("stock", 0),
            "sku": p.get("sku", ""),
            "image": p.get("image", ""),
            "quantity": p.get("quantity", 0)
        }
        for p in products
    ]

@router.post("/", response_model=Product)
def add_product(product: ProductIn):
    db = get_db()
    result = db.products.insert_one(product.dict())
    return {**product.dict(), "id": str(result.inserted_id)}

@router.delete("/{product_id}")
def delete_product(product_id: str):
    db = get_db()
    result = db.products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Deleted"}
