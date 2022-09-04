from fastapi.testclient import TestClient

from app.main import main_app

client = TestClient(main_app)


def test_alive_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}
