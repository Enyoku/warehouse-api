from fastapi import APIRouter

from router import item, user

router = APIRouter()

router.include_router(item.router)
router.include_router(user.router)
