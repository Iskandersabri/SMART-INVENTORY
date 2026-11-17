from app.schemas import ProductCreate, CategoryCreate, InventoryCreate
from app.models import Product, Category, Inventory


def addProduct(product: ProductCreate, database):
    new = Product(name= product.name, sku= product.sku, price= product.price, description= product.description, category_id= product.category_id)
    database.add(new)
    database.commit()
    database.refresh(new)

    return new

def addCategory(category : CategoryCreate, database):
    new = Category(name = category.name)
    database.add(new)
    database.commit()
    database.refresh(new)

    return new

def addInventory(inventory : InventoryCreate, database):
    new = Inventory(product_id= inventory.product_id, quantity= inventory.quantity, min_stock= inventory.min_stock, max_stock= inventory.max_stock)
    database.add(new)
    database.commit()
    database.refresh(new)

    return new