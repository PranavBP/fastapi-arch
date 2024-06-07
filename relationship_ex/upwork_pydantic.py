from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime



# Proposal Pydantic Models
class ProposalBase(BaseModel):
    content: str

class ProposalCreate(ProposalBase):
    pass

class Proposal(ProposalBase):
    id: int
    submitted_at: datetime
    user_id: int
    job_id: int

    class Config:
        orm_mode = True
   


# Job Pydantic Models

class JobBase(BaseModel):
    title: str
    description: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    posted_at: datetime
    owner_id: int
    proposals: List[Proposal] = []

    class Config:
        orm_mode = True



# User Pydantic Models     
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    jobs: List[Job] = []
    proposals: List[Proposal] = []

    class Config:
        orm_mode = True
