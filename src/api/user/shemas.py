from pydantic import BaseModel, EmailStr
from typing import Optional, List

from src.api.comments.schemas import Comment


class UserBase(BaseModel):
    username: str
    email: EmailStr
    homepage: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    comments: List[Comment] = []

