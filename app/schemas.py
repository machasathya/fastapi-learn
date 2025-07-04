from pydantic import BaseModel
from typing import Optional, List



class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class PostOut(BaseModel):
    title: str
    content: str
    published: bool
