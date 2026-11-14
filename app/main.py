from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app import models  # noqa: F401
from app.database import Base, engine


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
    return {"status": "ok", "message": "Smart Inventory API"}
