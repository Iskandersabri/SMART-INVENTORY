from fastapi import FastAPI

app = FastAPI(title="Smart Inventory")

@app.get("/")
def root():
    return {"status": "ok", "message": "Smart Inventory API"}