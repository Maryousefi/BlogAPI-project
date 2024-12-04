from pydantic import BaseModel
from typing import List
from datetime import datetime

#blog schemas(User Roles and Permissions)
class BlogPostBase(BaseModel):
    title: str
    content: str
    tags: List[str]

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

#user schemas
class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

#comment schemas
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    author_id: int
    blog_post_id: int

    class Config:
        orm_mode = True
