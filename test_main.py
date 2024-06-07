import pytest
from test_db import test_client
    
def test_create_car(test_client):
    response = test_client.post(
        "/api/v1/cars", json={"name": "Challenger","brand": "Dodge","year": 2020,"country": "USA","vin": "Challenger12345"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Challenger"
    assert response.json()["brand"] == "Dodge"
    
def test_get_cars(test_client):
    response = test_client.get("/api/v1/cars/")
    assert response.status_code == 200
    cars = response.json()
    assert isinstance(cars, list)
    assert len(cars) > 0 
    
def test_get_car_by_id(test_client):
    response = test_client.get("/api/v1/cars/1")
    assert response.status_code == 200
    car = response.json()
    assert car["name"] == "CX5"
    assert car["brand"] == "Mazda"
    
def test_update_car(test_client):
    response = test_client.put(
        "api/v1/cars/2", json={"name": "Forester", "brand": "Subaru", "year": 2021, "country": "USA"}
    )
    assert response.status_code == 200
    updated_car = response.json()
    assert updated_car["name"] == "Forester"
    assert updated_car["year"] == 2021
    
def test_delete_car(test_client):
    response = test_client.delete("/api/v1/cars/7")
    assert response.status_code == 404
    assert response.json() == {"detail": "Car not found"}
    
    response = test_client.get("/api/v1/cars/7")
    assert response.status_code == 404