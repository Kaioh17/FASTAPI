from pydantic import BaseModel, EmailStr
from datetime import datetime 
from typing import Optional


## user schemas
class CreateUser(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime   
    model_config = {"from_attributes": True}

## schema
class PostBase(BaseModel):
    title: str 
    content: str 
    published: bool = True
    


class CreatePost(PostBase):
    pass
class Updatepost(PostBase):
    published: bool

class Post(PostBase):
    user_id: int
    id: int
    owner: UserOut
    
    model_config = {"from_attributes": True}
   



##login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None