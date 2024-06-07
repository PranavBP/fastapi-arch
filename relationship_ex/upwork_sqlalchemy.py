from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    # Relationships
    jobs = relationship('Job', back_populates='owner')
    proposals = relationship('Proposal', back_populates='user')

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    posted_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    owner = relationship('User', back_populates='jobs')
    proposals = relationship('Proposal', back_populates='job')

class Proposal(Base):
    __tablename__ = 'proposals'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    # Relationships
    user = relationship('User', back_populates='proposals')
    job = relationship('Job', back_populates='proposals')

# Creating the database engine
engine = create_engine('sqlite:///upwork_clone.db')

# Creating all tables
Base.metadata.create_all(bind=engine)

# Creating a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Example usage
def create_sample_data():
    session = SessionLocal()
    user = User(username='john_doe', email='john@example.com', password='password')
    job = Job(title='Build a website', description='Looking for a developer to build a website.', owner=user)
    proposal = Proposal(content='I can build this website for you.', user=user, job=job)
    
    session.add(user)
    session.add(job)
    session.add(proposal)
    session.commit()
    session.close()

create_sample_data()
