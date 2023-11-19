from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Expense(BaseModel):
    account: str
    category: str
    description: str | None = None
    amount: float | int


@router.post("/expenses/direct")
async def expense_handler(expense: Expense):
    return {"status": 200, "expense": expense}
