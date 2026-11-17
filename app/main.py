from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import models  # noqa: F401
from app.database import Base, engine, get_db

from app.schemas import ProductCreate
from app.services import addProductServ


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