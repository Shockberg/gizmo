from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_status_endpoint():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Gizmo",
        "version": "0.1.0",
        "status": "running",
    }
