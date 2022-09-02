from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ItemBase(BaseModel):
    item_name: str
    article: int
    category: str
    price: int
    description: str
    amount: int


class ItemDisplay(BaseModel):
    article: int
    item_name: str
    category: str
    price: int

    class Config:
        orm_mode = True


class ItemList(ItemBase):
    id: Optional[int]
    updated_on: Optional[datetime]
