from app.repositories import addProduct
from app.schemas import ProductCreate

def addProductServ(productIn : ProductCreate, databaseIn):
    return addProduct(product= productIn, database=databaseIn)