from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql import func, text
from sqlalchemy.types import TIMESTAMP



class Posts(Base):
    __tablename__ = 'posts'  # Define the table name
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)    
    published = Column(Boolean, default=True)
    content = Column(String(225), nullable=False)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(225),nullable=False,unique=True)
    password = Column(String(225),nullable =False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)    