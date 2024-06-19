from sqlalchemy import select, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.api.comments.model import Comment
from src.api.comments.schemas import CommentCreate


class CommentService:
    @staticmethod
    async def get_comment(comment_id: int, session: AsyncSession):
        stmt = await session.execute(select(Comment).where(Comment.id == comment_id))
        return stmt.scalar_one_or_none()

    @staticmethod
    async def get_comments(skip: int = 0, limit: int = 25, order_by: str = "desc",
                           sort_field: str = "response_at", session: AsyncSession = None):
        sort_func = desc if order_by == "desc" else asc

        if sort_field not in ["username", "email", "response_at"]:
            sort_field = "response_at"

        stmt = (select(Comment).options(joinedload(Comment.replies)).where(Comment.parent_id == None).order_by
                (sort_func(getattr(Comment, sort_field))).offset(skip).limit(limit))

        result = await session.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def create_comment(comment: CommentCreate, user_id: int, session: AsyncSession):
        db_comment = Comment(content=comment.content, username=comment.username,
                             user_id=user_id, parent_id=comment.parent_id)
        session.add(db_comment)
        await session.commit()
        await session.refresh(db_comment)
        return db_comment
