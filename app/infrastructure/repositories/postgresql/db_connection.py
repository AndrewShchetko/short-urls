from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import PostgresSettings

config = PostgresSettings()

SQL_DATABASE_URL = f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:5432/{config.name}"
# SQL_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@postgres:5432/postgres"
engine = create_async_engine(SQL_DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
metadata = Base.metadata
