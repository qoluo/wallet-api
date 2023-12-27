from fastapi import APIRouter, Query, status
from typing import Annotated
from pydantic import BaseModel

router = APIRouter()


class Record(BaseModel):
    type: str
    account: str
    amount: Annotated[float | int, Query(gt=0)]
    currency: str
    date: str

@router.post("/records/add-income", status_code=status.HTTP_201_CREATED)
async def expense_handler(income: Record):
    return {"status": 200, "expense": income}

@router.post("/records/add-expense", status_code=status.HTTP_201_CREATED)
async def expense_handler(expense: Record):
    return {"status": 200, "expense": expense}
