from app.repositories import addProduct, addCategory, addInventory
from app.schemas import ProductCreate, CategoryCreate, InventoryCreate

def addProductServ(productIn : ProductCreate, databaseIn):
    return addProduct(product= productIn, database=databaseIn)

def addCategoryServ(categoryIn: CategoryCreate, databaseIn):
    return addCategory(category=categoryIn, database= databaseIn)

def addInventoryServ(inventoryIn: InventoryCreate, databaseIn):
    return addInventory(inventory=inventoryIn, database= databaseIn)