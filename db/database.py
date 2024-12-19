# from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config import settings

# sync_engine = create_engine(
#     url=settings.DATABASE_URL_psycopg,
#     echo=False,
#     pool_size=5,
#     max_overflow=10,
# )

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
