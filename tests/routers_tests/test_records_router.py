from fastapi.testclient import TestClient
from app.routers.records import router

client = TestClient(router)


def test_direct_expense():
    json = {
        "type": "income",
        "account": "first",
        "amount": 10,
        "currency": "EUR",
        "date": "123123",
    }

    response = client.post("/records/add-income", json=json)
    assert response.status_code == 201
    assert response.json() == {"status": "Success", "type": "income"}
