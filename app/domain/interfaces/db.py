from abc import ABC, abstractmethod

from app.domain.entities.original_url import OriginalURLBase
from app.domain.entities.short_url import ShortURLBase


class DBOperations(ABC):
    @abstractmethod
    async def get_original_url(self, short_url: str) -> OriginalURLBase:
        pass

    @abstractmethod
    async def check_short_url(self, short_url: str):
        pass

    @abstractmethod
    async def insert_original_url(self, original_url: str) -> int:
        pass

    @abstractmethod
    async def insert_short_url(self, original_url_id: int, short_url: ShortURLBase) -> ShortURLBase:
        pass
