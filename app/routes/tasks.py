from fastapi import APIRouter,HTTPException,Depends,status
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID,uuid4

from app.schema.taskschema import *
from app.schema.userschema import *
from app.models import Task,User
from app.database import SessionLocal
from app.exception import TaskNotFoundExpection

router=APIRouter()
tasks_db : List[Task_response]=[]

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create",response_model=Taskcreateresponse, status_code=status.HTTP_201_CREATED)
def create_task(task : TaskCreate, db :Session =Depends(get_db)):
    task_id=str(uuid4())
    db_task= Task(id=task_id, name=task.name, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"message" : "hey chetan , created successfully"}

@router.get("/", response_model=Tasklistresponse ,status_code=status.HTTP_200_OK)
def get_all_tasks(db :Session =Depends(get_db)):
    tasks_db=db.query(Task).all()
    return{ "message":"all tasks fetched",
           "data": tasks_db}

@router.get("/{task_id}", response_model=TaskbyID ,status_code=status.HTTP_200_OK)
def get_task_by_id(task_id :str , db :Session =Depends(get_db)):
    tasks_db=db.query(Task).all()

    if not tasks_db:
        raise TaskNotFoundExpection

    else:
        for task in tasks_db:
            if task.id==task_id:
                return { "message":"data found","data":task}

@router.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def Delete_task(task_id :str , db :Session =Depends(get_db)):
    tasks_db=db.query(Task).all()

    if not tasks_db:
        raise TaskNotFoundExpection
    
    else :
        for task in tasks_db:
            if task.id==task_id:
                db.delete(task)
                db.commit()
                db.refresh(tasks_db)
                return { "message":"Task deleted successfully"}
        
@router.put("/update/{id}", response_model=TaskResponse)
def update_task(id: str, updated_task: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.name = updated_task.name
    task.description = updated_task.description
    db.commit()
    db.refresh(task)

    return task

@router.post("/create/bulk", response_model= Tasklistresponse ,status_code=status.HTTP_201_CREATED)
def Bulk_create(tasks : List[TaskCreate],db :Session =Depends(get_db)):
    for task in tasks:
        task_id=str(uuid4())
        db_task= Task(id=task_id, name=task.name, description=task.description)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        
    task_db = db.query(Task).all()
    return{ "message":"all tasks fetched",
           "data":task_db }

@router.patch("/update/status/{id}", response_model=Taskupdateresponse,status_code=status.HTTP_200_OK)
def update_status(id : str , db :Session =Depends(get_db) ):
    task = db.query(Task).filter(Task.id == id).first()
    
    if not task:
        raise TaskNotFoundExpection
    
    else :
        task.completed = 1
        db.commit()
        db.refresh(task)
    
    return {"message" : "status updated successfully", "data":task}

@router.get("/completedtasks/",response_model=Tasklistresponse)
def get_completed_tasks(db: Session =Depends(get_db)):
    db_tasks=db.query(Task).filter(Task.completed == 1)

    return {"message" : "All completed tasks","data":db_tasks}

@router.post("/sorted", response_model=Tasklistresponse)
def get_sorted_tasks(desc: bool = False, db: Session = Depends(get_db)):
    order = Task.created_at.desc() if desc else Task.created_at.asc()
    tasks = db.query(Task).order_by(order).all()
    print(tasks)
    return {
        "message": "tasks sorted list",
        "data": tasks
    }