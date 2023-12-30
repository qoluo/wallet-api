from dotenv import load_dotenv
import os
from pymongo import MongoClient, timeout

load_dotenv()

db_uri: str = os.getenv("MONGODB_URL")


def get_db_client() -> MongoClient:
    return MongoClient(db_uri, connectTimeoutMS=2000, timeoutMS=2000)