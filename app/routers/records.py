from fastapi import APIRouter, Query, status, Response
from typing import Annotated
from pydantic import BaseModel
from app.routers.records_util.records_handler import add_record
from app.routers.records_util.records_handler import get_all_records

router = APIRouter()


class Record(BaseModel):
    type: str
    account: str
    amount: Annotated[float | int, Query(gt=0)]
    currency: str
    date: str


@router.post("/records/add-record", status_code=status.HTTP_201_CREATED)
async def expense_handler(record: Record, response: Response):
    record_data = record.model_dump()
    insert_result: bool = add_record(record_data)

    if not insert_result:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "Failed", "recordType": record_data["type"]}

    return {"status": "Success", "recordType": record_data["type"]}


@router.post("/records/aggregate", status_code=status.HTTP_200_OK)
async def aggregate_handler():
    records = get_all_records()
    return records
