from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Text, Integer, insert, select, engine
import time
import random
import routers.users

from util.db import DB
from fastapi import FastAPI

app = FastAPI()
app.include_router(routers.users.router)
DB.ensure_model_tables()

@app.get("/")
async def root():
    return {"message": "Helldsfasasdfasfddfo World"}