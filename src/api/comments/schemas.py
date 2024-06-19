from pydantic import BaseModel
from datetime import datetime


class CommentBase(BaseModel):
    content: str
    username: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    response_at: datetime
    user_id: int
