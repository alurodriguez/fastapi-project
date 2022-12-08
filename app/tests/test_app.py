from app.db.di import SQLiteDB
from app.deps import get_db
from app.main import app
from fastapi.testclient import TestClient


def get_test_db():
    try:
        session = SQLiteDB("sqlite:///./test.db").get_session()
        session = session()
        yield session
    finally:
        session.close()


app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id
