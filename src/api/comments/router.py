from fastapi import Depends, HTTPException, Query, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.comments.logic import CommentService
from src.api.comments.schemas import CommentBase, CommentCreate
from src.core.db.base import get_async_session

comment = APIRouter(
    prefix="/comment",
    tags=["comment"]
)


@comment.get("/comments/{comment_id}", response_model=CommentBase)
async def read_comment(comment_id: int, db: AsyncSession = Depends(get_async_session)):
    comment = await CommentService.get_comment(comment_id, db)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@comment.get("/comments/", response_model=list[CommentBase])
async def read_comments(
    skip: int = 0,
    limit: int = 25,
    order_by: str = Query("desc", regex="^(asc|desc)$"),
    sort_field: str = Query("response_at", regex="^(username|email|response_at)$"),
    db: AsyncSession = Depends(get_async_session)
):
    comments = await CommentService.get_comments(skip=skip, limit=limit, order_by=order_by,
                                                 sort_field=sort_field, session=db)
    return comments


@comment.post("/comments/", response_model=CommentBase)
async def create_comment(comment: CommentCreate, user_id: int, db: AsyncSession = Depends(get_async_session)):
    return await CommentService.create_comment(comment=comment, user_id=user_id, session=db)
