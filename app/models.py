from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID
from app.database import Base
from sqlalchemy import Column,String



class Task(Base):
    __tablename__= "tasks"

    id = Column(String(60),primary_key=True,index=True)
    name=Column(String(50))
    description = Column(String(255))






class Task_response(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class Createreponse(BaseModel):
    message: str
    data: List[Task_response]

class Tasklist(BaseModel):
    message: str
    data: List[Task_response]

class TaskbyID(BaseModel):
    message: str
    data: Task_response

