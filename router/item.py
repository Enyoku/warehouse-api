from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db

router = APIRouter(prefix="/warehouse", tags=["Item"])


@router.get("/items")
def get_all_items():
    return {}
