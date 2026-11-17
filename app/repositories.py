from app.schemas import ProductCreate, CategoryCreate
from app.models import Product, Category


def addProduct(product: ProductCreate, database):
    new = Product(name= product.name, sku= product.sku, price= product.price, description= product.description, category_id= product.category_id)
    database.add(new)
    database.commit()
    database.refresh(new)

    return new

def addCategory(category : CategoryCreate, database):
    new = Category()