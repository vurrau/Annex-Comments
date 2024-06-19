from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class CommentBase(BaseModel):
    content: str
    username: str


class CommentCreate(CommentBase):
    parent_id: Optional[int] = None


class Comment(CommentBase):
    id: int
    response_at: datetime
    user_id: int
    parent_id: Optional[int] = None
    replies: list['Comment'] = []
