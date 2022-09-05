from fastapi import HTTPException, status

from .database import database
from warehouse.schemas import ItemBase
from warehouse.model import item


async def create_item(request: ItemBase):
    new_item = item.insert().values(**request.dict())
    id = await database.execute(new_item)
    return {"id": id, **request.dict()}


async def get_all_items():
    return await database.fetch_all(query=item.select())


async def update_item(id: int, request: ItemBase):
    upd_item = item.update().where(item.c.id == id).values(**request.dict())
    return await database.execute(upd_item)


async def delete_item(id: int):
    del_item = item.delete().where(item.c.id == id)
    return await database.execute(del_item)
