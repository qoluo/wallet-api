from fastapi import FastAPI
from app.routers import records

app = FastAPI()

app.include_router(records.router)
