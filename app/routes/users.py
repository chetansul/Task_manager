from fastapi import APIRouter,HTTPException,Depends,status
from typing import List
from app.models import Task,User
from uuid import UUID,uuid4
from sqlalchemy.orm import Session

from app.schema.taskschema import *
from app.schema.userschema import *
from app.database import SessionLocal
from app.exception import TaskNotFoundExpection
from app.utils import hash_password,verify_password

router=APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/create", response_model=userscreate, status_code=status.HTTP_200_OK)
def create_user(user: userbase, db: Session = Depends(get_db)):

    check_email = db.query(User).filter(User.email == user.email).first()
    check_username= db.query(User).filter(User.username == user.username).first()
    #print(check_user.email)
    if check_email:
        return {
            "message": "email already there",
            "data": None
        }
    elif check_username:
        return {
            "message": "username already there",
            "data": None
        }
    

    user_id = str(uuid4())
    secure_password = hash_password(user.password)

    add_user = User(
        id=user_id,
        username=user.username,
        password=secure_password,
        email=user.email
    )

    db.add(add_user)
    db.commit()
    db.refresh(add_user)

    return {
        "message": "user created successfully",
        "data": add_user
    }

@router.post("/login",response_model=loginsuccess)
def user_login( user_detail : loginrequest ,db :Session =Depends(get_db) ):
    user_data = db.query(User).filter (user_detail.email == User.email ).first()

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(user_detail.password, user_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return { "message" :f"user logged in successfully , hey {user_data.username} welcome",}