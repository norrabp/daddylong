from fastapi import APIRouter

from app.auth.api import router as auth_router
from app.item.api import router as item_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(item_router, prefix="/items", tags=["items"])
