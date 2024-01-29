from sqlalchemy import Column, Text, UUID, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, UUID, DateTime

Base = declarative_base()
class Services(Base):
    __tablename__ = "services"
    id = Column(UUID, nullable=False, primary_key=True)
    name = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
