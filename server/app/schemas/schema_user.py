from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    mail: str
    password: str

class UserCreate(UserBase):
    pass

class User(BaseModel):
    userID: int
    

    class Config:
        orm_mode = True
