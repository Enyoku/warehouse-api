from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from user.schemas import UserDisplay, UserBase
from db import db_user
from auth import oauth2

router = APIRouter(prefix="/user", tags=["User"])


# Create user
@router.post("/create", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Get all users
@router.get("/all", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_current_user)):
    return db_user.get_all_users(db)


# Get user by id
@router.get("/{id}", response_model=UserDisplay)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, id)
