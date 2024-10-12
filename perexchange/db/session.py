from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from ..core.config import logger, settings

# Create the async engine with NullPool for SQLite
engine = create_async_engine(
    settings.DATABASE_URL,
    poolclass=NullPool,  # No pooling for SQLite
    echo=False,  # Set to True for SQL query logging
    future=True,
)

# Create a configured "Session" class
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database session error: {e}")
            raise
