from fastapi import HTTPException

from app.repositories import addProduct, addCategory, addInventory, getProductId, getCategoryId, getInventoryId
from app.schemas import ProductCreate, CategoryCreate, InventoryCreate

def addProductServ(productIn : ProductCreate, databaseIn):
    return addProduct(product= productIn, database=databaseIn)

def addCategoryServ(categoryIn: CategoryCreate, databaseIn):
    return addCategory(category=categoryIn, database= databaseIn)

def addInventoryServ(inventoryIn: InventoryCreate, databaseIn):
    return addInventory(inventory=inventoryIn, database= databaseIn)

def getProductServ(idIn: int, databaseIn):
    item = getProductId(id= idIn, database= databaseIn)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

def getCategoryServ(idIn: int, databaseIn):
    item = getCategoryId(id= idIn, database= databaseIn)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

def getInventoryServ(idIn: int, databaseIn):
    item = getInventoryId(id= idIn, database= databaseIn)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item



