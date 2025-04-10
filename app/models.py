from pydantic import BaseModel
from typing import Optional,List

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False 

class Createreponse(BaseModel):
    message: str
    data: List[Task]

class Tasklist(BaseModel):
    message: str
    data: List[Task]

class TaskbyID(BaseModel):
    message: str
    data: Task