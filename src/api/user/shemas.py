from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List

from src.api.comments.schemas import Comment


class UserBase(BaseModel):
    username: str
    email: EmailStr
    homepage: Optional[HttpUrl] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    comments: List[Comment] = []

