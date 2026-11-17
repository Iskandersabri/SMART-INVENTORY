from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config: 
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    description: str
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    description: str
    category_id: int

    class Config: 
        from_attributes = True

class InventoryCreate(BaseModel):
    product_id: int
    quantity: int
    min_stock: int
    max_stock: int

class InventoryResponse(BaseModel): 
    id: int
    product_id: int
    quantity: int
    min_stock: int
    max_stock: int

    class Config:  
        from_attributes = True