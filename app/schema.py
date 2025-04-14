from pydantic import BaseModel
from typing import List

# Schema for creating or updating a task
class TaskCreate(BaseModel):
    name: str
    description: str

class Taskcreateresponse(BaseModel):
    message:str
    
# Schema for returning a task (including its ID)
class TaskResponse(TaskCreate):
    id: str

    class Config:
        orm_mode = True

class Tasklistresponse(BaseModel):
    message :str
    data : List[TaskResponse]