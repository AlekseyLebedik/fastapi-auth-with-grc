from contextlib import asynccontextmanager
from typing import AsyncGenerator

from core.utils import _print
from settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    settings.DATABASE_URL_async,
    future=True,
    echo=True,
)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


@asynccontextmanager
async def getSession() -> AsyncGenerator:
    session_instance = None
    try:
        async with Session.begin() as session:
            session_instance: AsyncSession = session
            yield session_instance
    except:
        if session_instance:
            await session_instance.rollback()
        raise
    finally:
        if session_instance:
            await session_instance.close()
