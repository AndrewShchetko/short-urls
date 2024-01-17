from abc import abstractmethod

from app.domain.entities.short_url import ShortURLBase
from app.domain.interfaces.db import DBOperations
from .base_usecase import BaseUseCase


class MiddleUseCase(BaseUseCase):
    def __init__(self, repository: DBOperations):
        self.repository = repository

    @abstractmethod
    async def execute(self, *args, **kwargs) -> ShortURLBase:
        pass

    async def insert_url(self, original_url: str, short_url: str | None) -> ShortURLBase:
        async with self.repository as repo:
            await self.repository.check_short_url(short_url)
            original_url_id = await self.repository.insert_original_url(original_url)
            short_url_obj = await repo.insert_short_url(
                original_url_id,
                ShortURLBase(short_url=short_url)
            )
            return short_url_obj
