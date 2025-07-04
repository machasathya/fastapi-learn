from pydantic import BaseModel,EmailStr
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
    id : int
    title: str
    content: str
    published: bool



class User(BaseModel):
    email : EmailStr
    password :str
    
class UserOut(BaseModel):
    id: int
    email : EmailStr




class LoginCred(BaseModel):
    email : EmailStr
    password : str