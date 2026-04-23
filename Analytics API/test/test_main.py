from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_analyze_logs():
    response = client.post(
        "/analyze",
        json={
            "logs": [
                "INFO: User login",
                "ERROR: DB timeout",
                "ERROR: DB timeout"
            ]
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "INFO": 1,
        "ERROR": 2
    }