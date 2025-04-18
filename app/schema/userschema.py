from pydantic import BaseModel

class userbase(BaseModel):
    username :str
    password :str
    email :str

class userreposne(userbase):
    id  :str

    class config:
        orm_mode=True

class userscreate(BaseModel):
    message :str
    data : userreposne | None

class loginsuccess(BaseModel):
    message : str

class loginrequest(BaseModel):
    email :str
    password :str