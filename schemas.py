# PYDANTIC schemas
from pydantic import BaseModel

class CarBase(BaseModel):
    name: str
    brand: str
    year: int
    country: str
    
class CarCreate(CarBase):
    vin: str
    
class CarUpdate(CarBase):
    pass
    
class Car(CarBase):
    id: int
    
    class Config:
        orm_mode = True