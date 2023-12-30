from fastapi import FastAPI
from app.routers.records import router

app = FastAPI()

app.include_router(router)
