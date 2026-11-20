from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import models  # noqa: F401
from app.database import Base, engine, get_db

from app.schemas import ProductCreate, CategoryCreate, InventoryCreate
from app.services import addProductServ, addCategoryServ, addInventoryServ
from app.services import deleteProductServ, deleteCategoryServ, deleteInventoryServ
from app.services import updateProductServ


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Fail startup clearly if PostgreSQL is unavailable; Compose waits for health.
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    Base.metadata.create_all(bind=engine)
    yield



app = FastAPI(title="Smart Inventory API", lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "ok", "message": "HEY AMIGO   "}

@app.post('/Product')
def addProductRoot(product: ProductCreate, database : Session = Depends(get_db)):
    return addProductServ(productIn= product, databaseIn= database)

@app.post('/Category')
def addCategoryRoot(category: CategoryCreate, database : Session = Depends(get_db)):
    return addCategoryServ(categoryIn= category, databaseIn= database)

@app.post('/inventory')
def addInventoryRoot(inventory: InventoryCreate, database: Session = Depends(get_db)):
    return addInventoryServ(inventoryIn= inventory, databaseIn= database)

@app.delete('/Product/{product}')
def deleteProductRoot(product: int, database: Session = Depends(get_db)):
    return deleteProductServ(idIn= product, databaseIn=database)

@app.delete('/Category/{category}')
def deleteCategoryRoot(category: int, database: Session = Depends(get_db)):
    return deleteCategoryServ(idIn= category, databaseIn=database)

@app.delete('/Inventory/{inventory}')
def deleteInventoryRoot(inventory: int, database: Session = Depends(get_db)):
    return deleteInventoryServ(idIn= inventory, databaseIn=database)

@app.put('/Product/{productId}')
def updateProductRoot(productId: int, product = ProductCreate,database : Session = Depends(get_db)):
    product.id = productId
    return updateProductServ(new= product, databaseIn= database)


