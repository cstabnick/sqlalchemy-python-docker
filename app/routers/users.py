from fastapi import APIRouter, HTTPException
from uuid import UUID 
from models.user import Users 
from util.db import DB
from sqlalchemy.orm.session import Session
from sqlalchemy import select, text

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users():
    return []

@router.get("/{user_id}")
async def get_user(user_id: UUID):
    with DB.get_session() as session:
        session: Session
        user = session.execute(select(Users).filter_by(id=user_id)).fetchone()
        return user._asdict()