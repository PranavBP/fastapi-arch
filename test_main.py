import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    yield client
    
# def test_create_car(test_client):
#     response = test_client.post(
#         "/api/v1/cars", json={"name": "CX9","brand": "Mazda","year": 2020,"country": "USA","vin": "potryue"}
#     )
#     assert response.status_code == 200
#     assert response.json()["name"] == "CX9"
#     assert response.json()["brand"] == "Mazda"
    
def test_get_cars(test_client):
    response = test_client.get("/api/v1/cars/")
    assert response.status_code == 200
    cars = response.json()
    assert isinstance(cars, list)
    assert len(cars) > 0 
    
def test_get_car_by_id(test_client):
    response = test_client.get("/api/v1/cars/2")
    assert response.status_code == 200
    car = response.json()
    assert car["name"] == "CX9"
    assert car["brand"] == "Mazda"
    
def test_update_car(test_client):
    response = test_client.put(
        "api/v1/cars/1", json={"name": "Forester", "brand": "Subaru", "year": 2021, "country": "USA"}
    )
    assert response.status_code == 200
    updated_car = response.json()
    assert updated_car["name"] == "Forester"
    assert updated_car["year"] == 2021