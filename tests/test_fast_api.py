# test_fast_api.py

from fastapi.testclient import TestClient

from concord.fast_api import app

client = TestClient(app)


def test_root_endpoint_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Concord API"}


def test_root_endpoint_handles_get_method():
    response = client.get("/")
    assert response.status_code == 200


def test_root_endpoint_handles_post_method():
    response = client.post("/")
    assert response.status_code == 405
