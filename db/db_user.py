from sqlalchemy.orm import Session

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
