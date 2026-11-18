
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

def getProductId(id: int, database):
    item = database.query(Product).filter(Product.id == id).first()

    return item

def getCategoryId(id: int, database):
    item = database.query(Category).filter(Category.id == id).first()

    return item

def getInventoryId(id: int, database):
    item = database.query(Inventory).filter(Inventory.id == id).first()

    return item

def getInventoryProductId(product_id: int, database):
    return database.query(Inventory).filter(Inventory.product_id == product_id).first()

def deleteProduct(product: Product, database):
    database.delete(product)
    database.commit()

    return None

def deleteInventory(inventory: Inventory, database):
    database.delete(inventory)
    database.commit()

    return None

def deleteCategory( category : Category, database):
    database.delete(category)
    database.commit()

    return None
