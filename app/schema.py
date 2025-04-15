from pydantic import BaseModel
from typing import List, Optional

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

class Taskupdateresponse(BaseModel):
    message:str
    data : Task_response