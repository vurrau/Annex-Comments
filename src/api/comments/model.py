from datetime import datetime
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from src.core.db.base import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String, nullable=False)
    username = Column(String(length=30), nullable=False)
    response_at = Column(DateTime, default=datetime)
