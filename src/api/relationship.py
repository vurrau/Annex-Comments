from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.core.db.base import Base


class User(Base):

    comment = relationship("Comment", back_populates="user")


class Comment(Base):

    username = relationship("User", back_populates="comment")


