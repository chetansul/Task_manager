from fastapi import FastAPI
from app.routes import tasks,users

app=FastAPI()
app.include_router(tasks.router, prefix="/tasks")
app.include_router(users.router,prefix="/users")
