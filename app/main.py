
from sqlalchemy.orm import declarative_base
from sqlalchemy import (Column, Text, Integer, insert, select, engine)
import time
import random

from util.db import DB

Base = declarative_base()


class Animals(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)

Animals.__table__.create(bind=DB.get_engine(), checkfirst=True)

rand_id = random.randint(0, 10000)
ins = (
    insert(Animals).
    values(id = rand_id, name=f"test {rand_id}")
)
sel = select(Animals)


DB.insert_one(ins)
print(DB.select_many(sel))
