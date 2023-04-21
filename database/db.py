from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import Config

engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URL, poolclass=NullPool)


async def get_session():
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        finally:
            await session.close()
