import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base
from app.main import get_db

POSTGRES_TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost/test_biblioteca"
engine = create_engine(POSTGRES_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


def test_create_book(client):
    response = client.post("/books/", json={
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "isbn": "1234567890123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "1984"
    assert data["author"] == "George Orwell"


def test_list_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


def test_update_book(client):
    response = client.put("/books/1", json={
        "title": "1984 (Updated)",
        "author": "George Orwell",
        "year": 1950,
        "isbn": "1234567890123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "1984 (Updated)"
    assert data["year"] == 1950


def test_delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 204
    response = client.get("/books/")
    data = response.json()
    assert len(data) == 0
