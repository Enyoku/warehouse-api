from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_cheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: dict = Depends(oauth2_cheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    return token.verify_token(data, credentials_exception)
