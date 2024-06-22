from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.db.base import Base
from src.api.comments.model import Comment


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=30), nullable=False)
    email = Column(String(length=30), nullable=False)
    homepage = Column(String, nullable=True)
    comments = relationship("Comment", back_populates="user")
