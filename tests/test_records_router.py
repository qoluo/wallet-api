from fastapi.testclient import TestClient

from routers.records import router

client = TestClient(router)


def test_direct_expense():
    json = {
        "account": "test-acc",
        "category": "test-cat",
        "amount": 123
    }

    response = client.post("/expenses/direct", json=json)
    assert response.status_code == 200
    assert response.json() == {
        "status": 200,
        "expense": {
            "account": "test-acc",
            "category": "test-cat",
            "description": None,
            "amount": 123.0
        }
    }
