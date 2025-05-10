from pydantic import BaseModel
from typing import Optional

class ProductIn(BaseModel):
    name: str
    price: float
    category: Optional[str] = ""
    description: Optional[str] = ""
    stock: Optional[int] = 0
    sku: Optional[str] = ""
    image: Optional[str] = ""
    quantity: int

class Product(ProductIn):
    id: str
