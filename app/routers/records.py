from fastapi import APIRouter, Query, status, Response
from typing import Annotated
from pydantic import BaseModel
from app.routers.records_util.records_handler import add_record

router = APIRouter()


class Record(BaseModel):
    type: str
    account: str
    amount: Annotated[float | int, Query(gt=0)]
    currency: str
    date: str


@router.post("/records/add-income", status_code=status.HTTP_201_CREATED)
async def expense_handler(income: Record, response: Response):
    record_data = income.model_dump()
    insert_result: bool = add_record(record_data)

    if not insert_result:
        response.status_code: str = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
        "status": "Failed",
        "recordType": "income"
    }

    return {
        "status": "Success",
        "type": "income"
    }


@router.post("/records/add-expense", status_code=status.HTTP_201_CREATED)
async def expense_handler(expense: Record):
    return {"status": 200, "expense": expense}
