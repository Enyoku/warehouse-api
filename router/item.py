from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from warehouse.schemas import ItemBase, ItemDisplay
from db import db_items

router = APIRouter(prefix="/warehouse", tags=["Item"])


@router.post("/new", response_model=ItemDisplay)
def create_item(request: ItemBase, db: Session = Depends(get_db)):
    return db_items.create_item(db, request)
    # return f"Item {request.item_name} created"


@router.get("/all", response_model=List[ItemDisplay])
def get_all_items(db: Session = Depends(get_db)):
    return db_items.get_all_items(db)


@router.put("/{id}")
def update_item(id: int, request: ItemBase, db: Session = Depends(get_db)):
    return db_items.update_item(id, request, db)


@router.delete("/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    return db_items.delete_item(id, db)
