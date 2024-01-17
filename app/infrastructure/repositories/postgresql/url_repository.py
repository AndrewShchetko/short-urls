from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.domain.entities.original_url import OriginalURLBase
from app.domain.entities.short_url import ShortURLBase
from app.domain.interfaces.db import DBOperations
from app.infrastructure.models.models import OriginalURL, ShortURL
from .db_connection import SessionLocal, AsyncSession


class URLRepository(DBOperations):
    async def __aenter__(self):
        self.session: AsyncSession = SessionLocal()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.session.commit()
        except exc_type:
            await self.session.rollback()
        finally:
            await self.session.close()

    async def get_original_url(self, short_url: str) -> OriginalURLBase:
        long_url_obj = await self.session.execute(
            select(OriginalURL)
            .join(ShortURL, ShortURL.long_url_id == OriginalURL.id)
            .options(joinedload(OriginalURL.short_urls))
            .where(ShortURL.short_url == short_url)
        )
        if long_url_obj := long_url_obj.unique().scalars().one_or_none():
            return OriginalURLBase(long_url=long_url_obj.long_url)
        else:
            return long_url_obj

    async def check_short_url(self, short_url: str):
        short_url_obj = await self.session.execute(
            select(OriginalURL)
            .filter(ShortURL.short_url == short_url)
        )
        if short_url_obj.scalars().one_or_none():
            raise HTTPException(status_code=400, detail="Short url is already exists")

    async def insert_original_url(self, original_url: str) -> int:
        db_url = await self.session.execute(
            select(OriginalURL)
            .filter(OriginalURL.long_url == original_url)
        )
        if db_url := db_url.scalars().one_or_none():
            return db_url.id
        long_url_obj = OriginalURL(long_url=original_url)
        self.session.add(long_url_obj)
        return long_url_obj.id

    async def insert_short_url(self, original_url_id: int, short_url: ShortURLBase) -> ShortURLBase:
        short_url_obj = ShortURL(short_url=short_url.short_url, long_url_id=original_url_id)
        self.session.add(short_url_obj)
        return ShortURLBase(short_url=short_url_obj.short_url)
