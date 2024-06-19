from datetime import datetime
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.core.db.base import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    parent_id = Column(Integer, ForeignKey('comment.id'), nullable=True)  # Добавляем поле для каскадного отображения
    content = Column(String, nullable=False)
    username = Column(String(length=30), nullable=False)
    response_at = Column(DateTime, default=datetime)
    user = relationship("User", back_populates="comments")
    replies = relationship("Comment", back_populates="parent", remote_side=[id])  # Добавляем связь для дочерних комментариев
    parent = relationship("Comment", back_populates="replies", remote_side=[id])  # Добавляем связь для родительских комментариев