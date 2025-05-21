from sqlalchemy import Column, Integer, String, Boolean
from app.db.connection import Base

class Monster(Base):
    __tablename__ = "monsters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, nullable=True)
    element = Column(String, nullable=True)
    species = Column(String, nullable=True)
    ailment = Column(String, nullable=True)
    is_large = Column(Boolean)
