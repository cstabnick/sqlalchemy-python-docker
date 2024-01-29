from fastapi import APIRouter
from uuid import UUID 

router = APIRouter()

@router.get("users", tags=["users"])
async def get_users():
    return []

@router.get("users/{user_id}", tags=["users"])
async def get_user(user_id: UUID):
    pass