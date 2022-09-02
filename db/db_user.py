from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from user.schemas import UserBase
from user.models import User
from core.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        full_name=request.full_name,
        position=request.position,
        created_on=request.created_on
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def update_user_info(db: Session, id: int, request: UserBase):
    user = db.query(User).filter(User.id == id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.update({
        User.username: request.username,
        User.email: request.email,
        User.password: Hash.bcrypt(request.password),
        User.full_name: request.full_name,
        User.position: request.position,
        User.created_on: request.created_on
    })
    db.commit()
    return "ok"


def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    db.delete(user)
    db.commit()
    return "deleted"
