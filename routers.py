from fastapi import APIRouter

from router import item, user, authentication

router = APIRouter()

router.include_router(authentication.router)
router.include_router(user.router)
router.include_router(item.router)