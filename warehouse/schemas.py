from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BaseItem(BaseModel):
    item_name: str
    category: str
    price: int
    description: str
    amount: int


class ItemDisplay(BaseModel):
    item_id: int
    item_name: str
    category: str
    price: int


class ItemList(BaseItem):
    id: Optional[int]
    updated_on: Optional[datetime]
