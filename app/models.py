from .database import Base
from sqlalchemy import Column, Integer, String, Boolean



class Posts(Base):
    __tablename__ = 'posts'  # Define the table name
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(500), nullable=False)
    published = Column(Boolean, default=True)
