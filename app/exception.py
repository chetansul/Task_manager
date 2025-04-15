from fastapi import HTTPException ,status

class TaskNotFoundExpection(HTTPException):
    def __inti__(self):
        super().__init__(status_code=status.HTTP_204_NO_CONTENT , detail= "Task Not Found")