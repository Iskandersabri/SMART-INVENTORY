from fastapi import HTTPException

from app.repositories import addProduct, addCategory, addInventory
from app.repositories import  getProductId, getCategoryId, getInventoryId, getInventoryProductId
from app.repositories import deleteProduct, deleteInventory, deleteCategory
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

def deleteProductServ(idIn: int, databaseIn):
    product = getProductServ(idIn=idIn, databaseIn= databaseIn)

    invId = getInventoryProductId(product_id= product.id, database= databaseIn)
    deleteInventoryServ(idIn= invId, databaseIn= databaseIn)
    return deleteProduct(product, databaseIn)

def deleteInventoryServ(idIn: int, databaseIn):
    inventory = getInventoryServ(idIn=idIn, databaseIn= databaseIn)

    return deleteInventory(inventory= inventory, database= databaseIn)

def deleteCategoryServ(idIn: int, databaseIn):
    category = getCategoryServ(idIn=idIn, databaseIn= databaseIn)

    return deleteCategory(category= category, database= databaseIn)

