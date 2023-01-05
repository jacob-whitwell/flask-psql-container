from typing import Union

from pydantic import BaseModel


# Create the required fields
class UserBase(BaseModel):
    id: int

class UserCreate(UserBase):
    firstname: str
    lastname: str

    class Config:
        orm_mode = True

class User(UserBase):
    firstname: str
    lastname: str

    class Config:
        orm_mode = True

class UserDelete(UserBase):
    id: int
    
    class Config:
        orm_mode = True