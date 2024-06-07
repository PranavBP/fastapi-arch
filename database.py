from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# A Local session created with an engine binded to it

# 1. Changed will not be auto commited, we need to manually commit.
# 2. Before certain ops the autoflush will flush the db before a query runs, 
# Flushing - syncronizing the state of in-memory objects in database
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# this returns a base class required for the sqlalchemy ORM model
Base = declarative_base()

# Dependency
'''
We need to have an independent database session/connection (SessionLocal) per request, 
use the same session through all the request and then close it after the request is finished.
And then a new session will be created for the next request.
'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

