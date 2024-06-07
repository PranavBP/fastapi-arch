# PYDANTIC schemas
from pydantic import BaseModel

# Attributes used while both reading and writing
class CarBase(BaseModel):
    name: str
    brand: str
    year: int
    country: str
    
# used while creating, inherits everything from Base class as well
class CarCreate(CarBase):
    vin: str
    
# used only while updating
class CarUpdate(CarBase):
    pass
    
# used only while reading
class Car(CarBase):
    id: int
    
    # Read the data even if not dict, but an ORM model - Enables Lazy loading, only load what is required.
    class Config:
        orm_mode = True