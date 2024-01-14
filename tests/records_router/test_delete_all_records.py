import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.routers.records import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


@pytest.fixture(autouse=True)
def add_multiple_records():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "amount": 123,
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    for _ in range(3):
        client.post("/records/add-record", json=json)


def test_delete_all_records():
    response = client.delete("/records/delete-all")
    assert response.status_code == 200
    assert response.json() is True


def test_delete_all_records_with_post():
    response = client.post("/records/delete-all")
    assert response.status_code == 405


def test_delete_all_records_with_put():
    response = client.put("/records/delete-all")
    assert response.status_code == 405


def test_delete_all_records_with_get():
    response = client.get("/records/delete-all")
    assert response.status_code == 405
