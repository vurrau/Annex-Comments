from sqlalchemy import Integer, String, Column, ForeignKey

from src.core.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=30), nullable=False)
    email = Column(String(length=30), nullable=False)
    comments = Column(Integer, ForeignKey('comment.id'))
