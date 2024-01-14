from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.routers.records import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_add_record_correctly():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "amount": 123,
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 201
    assert response.json() == {"status": "Success", "recordType": "pytest-type"}


def test_add_record_use_put():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "amount": 123,
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    response = client.put("/records/add-record", json=json)
    assert response.status_code == 405


def test_add_record_use_delete():
    response = client.delete("/records/add-record")
    assert response.status_code == 405


def test_add_record_use_get():
    response = client.get("/records/add-record")
    assert response.status_code == 405


def test_add_record_without_type_field():
    json = {
        "account": "pytest-account",
        "amount": 123,
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 422


def test_add_record_without_account_field():
    json = {
        "type": "pytest-type",
        "amount": 123,
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 422


def test_add_record_without_amount_field():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "currency": "pytest-currency",
        "date": "pytest-date",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 422


def test_add_record_without_currency_field():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "amount": 123,
        "date": "pytest-date",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 422


def test_add_record_without_date_field():
    json = {
        "type": "pytest-type",
        "account": "pytest-account",
        "amount": 123,
        "currency": "pytest-currency",
    }

    response = client.post("/records/add-record", json=json)
    assert response.status_code == 422


def test_add_record_without_any_data():
    response = client.post("/records/add-record", json={})
    assert response.status_code == 422
