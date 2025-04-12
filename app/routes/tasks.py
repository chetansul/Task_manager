from fastapi import APIRouter,HTTPException
from typing import List
from app.models import *

router=APIRouter()
tasks_db : List[Task]=[]


@router.post("/create",response_model=Createreponse)
def create_task(task : Task):
    task.id=uuid4()
    tasks_db.append(task)
    return {"message" : "hey chetan , created successfully",
            "data" : tasks_db}

@router.get("/tasks", response_model=Tasklist)
def get_all_tasks():
    return{ "message":"all tasks fetched",
           "data": tasks_db}


@router.get("/tasks/{task_id}", response_model=TaskbyID)
def get_task_by_id(task_id :UUID ):
    for task in tasks_db:
        if task.id==task_id:
            return { "message":"data found","data":task}
        
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/delete/{task_id}", response_model=Tasklist)
def Delete_task(task_id :UUID ):
    for task in tasks_db:
        if task.id==task_id:
            tasks_db.remove(task)
            return { "message":"Task deleted successfully","data":tasks_db}
        
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/update/{task_id}", response_model=Tasklist)
def update_task(task :Task , task_id :UUID):
    print(task_id)
    for t in tasks_db:
        if t.id==task_id:
            t.title= task.title
            t.description= task.description
            t.completed= task.completed
                    
            return { "message":"Task updated successfully","data":tasks_db}
        
    raise HTTPException(status_code=404, detail="Task not found")

