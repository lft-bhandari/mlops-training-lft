from pydantic import BaseModel

class UserTaskCreate(BaseModel):
    username: str
    designation: str
    tasks: str

class UserTaskResponse(UserTaskCreate):
    id: int

    class Config:
        from_attributes = True
