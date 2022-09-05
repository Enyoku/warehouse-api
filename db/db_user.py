from fastapi import HTTPException, status

from user.schemas import UserBase
from user.models import user
from core.hash import Hash
from db.database import database


async def create_user(request: UserBase):
    new_user = user.insert().values(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name,
        position=request.position,
        created_on=request.created_on
    )
    id = await database.execute(new_user)
    return {"id": id, **request.dict()}


async def get_all_users():
    return await database.fetch_all(user.select())


async def get_user_by_id(id: int):
    return await database.fetch_one(user.select().where(user.c.id == id))


async def update_user_info(id: int, request: UserBase):
    upd_user = user.update().where(user.c.id == id).values(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name,
        position=request.position,
        created_on=request.created_on
    )
    return await database.execute(upd_user)


async def delete_user(id: int):
    del_user = user.delete().where(user.c.id == id)
    return await database.execute(del_user)
