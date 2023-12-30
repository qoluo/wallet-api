import os
from app.db.connector import get_db_client
from pymongo import MongoClient

default_db_name: str = os.getenv("WALLET_DEFAULT_DB")
records_collection_name: str = os.getenv("WALLET_RECORDS_COLLECTION")


def add_record(record: dict[str, int]):
    db_client: MongoClient = get_db_client()

    if not db_client:
        return False

    wallet_default_db = db_client[default_db_name]
    collection = wallet_default_db[records_collection_name]

    result = collection.insert_one(record)
    db_client.close()

    return True if result.inserted_id else False
