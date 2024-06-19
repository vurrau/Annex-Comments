from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.user.logic import UserService
from src.api.user.shemas import UserBase, UserCreate
from src.core.db.base import get_async_session

user = APIRouter(
    prefix="/request",
    tags=["request"]
)


@user.get("/users/{user_id}", response_model=UserBase)
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    user = await UserService.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user.get("/users/", response_model=list[UserBase])
async def read_users(skip: int = 0, limit: int = 25, db: AsyncSession = Depends(get_async_session)):
    users = await UserService.get_users(skip=skip, limit=limit, session=db)
    return users


@user.post("/users/", response_model=UserBase)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    return await UserService.create_user(user=user, session=db)
