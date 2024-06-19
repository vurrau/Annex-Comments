from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.user.model import User
from src.api.user.shemas import UserCreate


class UserService:
    @staticmethod
    async def get_user(user_id: int, session: AsyncSession):
        stmt = await session.execute(select(User).where(User.id == user_id))
        return stmt.scalar_one_or_none()

    @staticmethod
    async def get_users(skip: int = 0, limit: int = 25, session: AsyncSession = None):
        stmt = await session.execute(select(User).offset(skip).limit(limit))
        return stmt.scalars().all()

    @staticmethod
    async def create_user(user: UserCreate, session: AsyncSession):
        db_user = User(username=user.username, email=user.email, homepage=user.homepage)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user
