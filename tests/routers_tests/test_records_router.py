from fastapi.testclient import TestClient

from app.routers.records import router

client = TestClient(router)


def add_record_test():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "amount": 123,
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 201
    assert response.json() == {"status": "Success", "recordType": "income"}


def test_direct_expense():
    json = {
        "type": "expense",
        "account": "second",
        "amount": 101.1,
        "currency": "EUR",
        "date": "22332",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 201
    assert response.json() == {"status": "Success", "recordType": "expense"}
