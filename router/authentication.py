from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from user.models import user
from core.hash import Hash
from auth import token
from db.database import database

router = APIRouter(tags=["Authentication"])


@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    cur_user = await database.fetch_one(query=user.select().where(user.c.username == request.username))
    if not cur_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials")
    if not Hash.verify(cur_user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password")

    access_token = token.create_access_token(data={"sub": cur_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
