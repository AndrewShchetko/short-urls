from abc import ABC, abstractmethod

from app.domain.entities.short_url import ShortURLBase


class BaseUseCase(ABC):
    @abstractmethod
    async def execute(self, *args, **kwargs) -> ShortURLBase:
        pass
