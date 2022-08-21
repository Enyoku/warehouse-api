from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    full_name: str
    position: str
    created_on: datetime


class UserDisplay(BaseModel):
    username: str
    position: str
    email: str

    class Config:
        orm_mode = True
