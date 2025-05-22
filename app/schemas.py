from pydantic import BaseModel, EmailStr
from datetime import datetime 
# schema
class PostBase(BaseModel):
    title: str 
    content: str 
    published: bool = True


class CreatePost(PostBase):
    pass
class Updatepost(PostBase):
    published: bool

class Post(PostBase):
    id: int
    model_config = {"from_attributes": True}

## user schemas
class CreateUser(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    model_config = {"from_attributes": True}

##login
class UserLogin(BaseModel):
    email: EmailStr
    password: str