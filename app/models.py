from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.sql import func, text
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import Relationship
from sqlalchemy.orm import relationship



class Posts(Base):
    __tablename__ = 'posts'  # Define the table name
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)    
    published = Column(Boolean, default=True)
    content = Column(String(225), nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("Users",back_populates="posts")


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(225),nullable=False,unique=True)
    password = Column(String(225),nullable =False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)    
    posts = relationship("Posts", back_populates="owner")