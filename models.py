# SQLAlchemy ORM Models

# Package imports
from sqlalchemy import Column, Boolean, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Internal imports
from database import Base

class Car(Base):
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    brand = Column(String, index=True)
    year = Column(Integer)
    country = Column(String)
    
 