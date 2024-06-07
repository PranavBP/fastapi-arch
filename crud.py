from sqlalchemy.orm import Session

from schemas import CarCreate, CarUpdate
from models import Car


class CarCrud:
    
    @staticmethod
    def get_car_by_id(db: Session, car_id: int):
        return db.query(Car).filter(Car.id == car_id).first()

    @staticmethod
    def get_car_by_name(db: Session, car_name: str):
        return db.query(Car).filter(Car.name == car_name).first()

    @staticmethod
    def get_cars(db: Session):
        # , skip: int, limit: int
        # return db.query(Car).offset(skip).limit(limit).all()
        return db.query(Car).all()

    @staticmethod
    def create_car(db:Session, car: CarCreate):
        db_car = Car(**car.model_dump())
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return db_car
    
    @staticmethod
    def update_car(db:Session, car_id: int, car: CarUpdate):
        db_car = db.query(Car).filter(Car.id == car_id).first()
        if db_car:
            for key, value in car.model_dump().items():
                print(key, value)
                setattr(db_car, key, value)
            db.commit()
            db.refresh(db_car)
        return db_car
    
    @staticmethod
    def delete_car(db: Session, car_id: int):
        db_car = db.query(Car).filter(Car.id == car_id).first()
        if db_car:
            db.delete(db_car)
            db.commit()
        return db_car