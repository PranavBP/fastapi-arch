# SQLAlchemy ORM Models - Object Relational Mapper 
# To convert and map objects in code to database relational tables.
# Each instance of this object will represnt a row in database table

# Package imports
from sqlalchemy import Column, Boolean, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Internal imports
from database import Base

class Car(Base):
    __tablename__ = "cars"
    
    # Indexing for faster search - using B-TREE - something like book with indexes to quickly search items.
    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    brand = Column(String, index=True)
    year = Column(Integer)
    country = Column(String)
    
 