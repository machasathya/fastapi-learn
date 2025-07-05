from pydantic import BaseModel,EmailStr
from typing import Optional
from pydantic.types import conint

class User(BaseModel):
    email : EmailStr
    password :str
    
class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    owner: UserOut  # Make sure this matches

    class Config:
        from_attributes = True  




class LoginCred(BaseModel):
    email : EmailStr
    password : str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None

class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)