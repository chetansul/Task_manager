from fastapi import APIRouter,HTTPException,Depends
from typing import List
from app.models import *
from uuid import UUID,uuid4
from app.schema import TaskCreate,TaskResponse,Tasklistresponse,Taskcreateresponse
from app.database import SessionLocal
from sqlalchemy.orm import Session

router=APIRouter()
tasks_db : List[Task_response]=[]

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create",response_model=Taskcreateresponse)
def create_task(task : TaskCreate, db :Session =Depends(get_db)):
    task_id=str(uuid4())
    db_task= Task(id=task_id, name=task.name, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"message" : "hey chetan , created successfully"}

@router.get("/tasks", response_model=Tasklistresponse)
def get_all_tasks(db :Session =Depends(get_db)):
    tasks_db=db.query(Task).all()
    return{ "message":"all tasks fetched",
           "data": tasks_db}


@router.get("/tasks/{task_id}", response_model=TaskbyID)
def get_task_by_id(task_id :str , db :Session =Depends(get_db)):
    tasks_db=db.query(Task).all()
    for task in tasks_db:
        if task.id==task_id:
            return { "message":"data found","data":task}
        
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/delete/{task_id}", response_model=Tasklistresponse)
def Delete_task(task_id :str , db :Session =Depends(get_db)):
    tasks_db=db.query(Task).all()
    for task in tasks_db:
        if task.id==task_id:
            db.delete(task)
            db.commit()
            db.refresh(tasks_db)
            return { "message":"Task deleted successfully","data":tasks_db}
        
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/update/{id}", response_model=TaskResponse)
def update_task(id: str, updated_task: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    print(task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.name = updated_task.name
    task.description = updated_task.description
    db.commit()
    db.refresh(task)

    return task