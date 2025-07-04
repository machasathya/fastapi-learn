from pydantic import BaseModel,EmailStr
from typing import Optional, List

class User(BaseModel):
    email : EmailStr
    password :str
    
class UserOut(BaseModel):
    id: int
    email : EmailStr
    class Config:
        orm_mode = True


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
    owner_id : int
    owner : UserOut
    class Config:
        orm_mode = True




class LoginCred(BaseModel):
    email : EmailStr
    password : str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None


