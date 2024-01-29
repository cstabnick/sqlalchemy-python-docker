from sqlalchemy import Column, Text, UUID, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, UUID, DateTime

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(UUID, nullable=False, primary_key=True)
    username = Column(Text)
    password = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
