from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from car_endpoint import router as car_router
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:49518",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=car_router, prefix="/api/v1", tags=["cars"])

@app.get("/")
def home():
    return {"message": "Welcome to demo app"}