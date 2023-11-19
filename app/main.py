from fastapi import FastAPI
from app.routers import records

app = FastAPI()

app.include_router(records.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
