
from uuid import UUID
from app.database import Base
from sqlalchemy import Column,String,Boolean,DateTime
from sqlalchemy.sql import func



class Task(Base):
    __tablename__= "tasks"

    id = Column(String(60),primary_key=True,index=True)
    name=Column(String(50))
    description = Column(String(255))
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__= "users"

    id = Column(String(60),primary_key=True,index=True)
    username=Column(String(50),nullable= False)
    password = Column(String(255),nullable = False)
    email = Column(String(255),nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())







