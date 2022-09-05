from typing import List

from fastapi import APIRouter, Depends

from warehouse.schemas import ItemBase, ItemDisplay
from db import db_items

router = APIRouter(prefix="/warehouse", tags=["Item"])


@router.post("/new", response_model=ItemDisplay)
async def create_item(request: ItemBase):
    return await db_items.create_item(request)


@router.get("/all", response_model=List[ItemDisplay])
async def get_all_items():
    return await db_items.get_all_items()


@router.put("/{id}")
async def update_item(id: int, request: ItemBase):
    return await db_items.update_item(id, request)


@router.delete("/{id}")
async def delete_item(id: int):
    return await db_items.delete_item(id)
