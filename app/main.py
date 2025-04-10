from fastapi import FastAPI,HTTPException
from typing import List
from app.models import *
app=FastAPI()

tasks_db : List[Task]=[]


@app.post("/create",response_model=Createreponse)
def create_task(task : Task):
    tasks_db.append(task)
    return {"message" : "hey chetan , created successfully",
            "data" : tasks_db}

@app.get("/tasks", response_model=Tasklist)
def get_all_tasks():
    return{ "message":"all tasks fetched",
           "data": tasks_db}


@app.get("/tasks/{task_id}", response_model=TaskbyID)
def get_all_tasks(task_id :int ):
    for task in tasks_db:
        if task.id==task_id:
            return { "message":"data found","data":task}
        
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/delete/{task_id}", response_model=Tasklist)
def get_all_tasks(task_id :int ):
    for task in tasks_db:
        if task.id==task_id:
            tasks_db.remove(task)
            return { "message":"Task deleted successfully","data":tasks_db}
        
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/update/{task_id}", response_model=Tasklist)
def get_all_tasks(task :Task ):
    for t in tasks_db:
        if t.id==task.id:
            t.id=task.id
            t.title= task.title
            t.description= task.description
            t.completed= task.completed
                    
            return { "message":"Task updated successfully","data":tasks_db}
        
    raise HTTPException(status_code=404, detail="Task not found")

