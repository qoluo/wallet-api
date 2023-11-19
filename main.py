from fastapi import FastAPI
from routers import records

app = FastAPI()

app.include_router(records.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
