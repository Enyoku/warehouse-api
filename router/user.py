from typing import List

from fastapi import APIRouter, Depends

from user.schemas import UserDisplay, UserBase
from db import db_user
from auth import oauth2

router = APIRouter(prefix="/user", tags=["User"])


# Create user
@router.post("/create", response_model=UserDisplay, tags=["Authentication"])
async def create_user(request: UserBase):
    return await db_user.create_user(request)


# Get all users
@router.get("/all", response_model=List[UserDisplay])
async def get_all_users():  # , current_user: UserBase = Depends(oauth2.get_current_user)):
    return await db_user.get_all_users()


# Get user by id
@router.get("/{id}", response_model=UserDisplay)
async def get_user_by_id(id: int):
    return await db_user.get_user_by_id(id)


# Update user info by id
@router.put("/update/{id}")
async def update_user(id: int, request: UserBase):
    return await db_user.update_user_info(id, request)


# Delete user
@router.delete("/{id}")
async def delete_user(id: int):
    return await db_user.delete_user(id)
