# package imports
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

# internal imports
from database import get_db
from schemas import Car, CarCreate, CarUpdate
from crud import CarCrud


router = APIRouter()

@router.get("/cars/", response_model=list[Car])
def get_cars(db: Session = Depends(get_db)):
    # skip: int, limit: int, 
    return CarCrud.get_cars(db=db)

@router.get("/cars/{car_id}", response_model=Car)
def get_car_by_id(car_id: int, db: Session = Depends(get_db)):
    db_car = CarCrud.get_car_by_id(db=db, car_id=car_id)
    if not db_car:
        raise HTTPException(404, f"Car not found")
    return db_car

@router.post("/cars/", response_model=Car)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = CarCrud.get_car_by_name(db=db, car_name=car.name)
    if db_car:
        raise HTTPException(400, "Car is already registered")
    return CarCrud.create_car(db=db, car=car)

@router.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: CarUpdate, db: Session = Depends(get_db)):
    db_car = CarCrud.get_car_by_id(db=db,car_id=car_id)
    if db_car is None:
        raise HTTPException(404, "Car not found")
    return CarCrud.update_car(db=db, car_id=car_id, car=car)

@router.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = CarCrud.get_car_by_id(db=db, car_id=car_id)
    if db_car is None:
        raise HTTPException(404, "Car not found")
    return CarCrud.delete_car(db=db, car_id=car_id)