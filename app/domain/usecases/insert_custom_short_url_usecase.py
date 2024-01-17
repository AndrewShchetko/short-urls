from app.domain.entities.short_url import ShortURLBase
from .middle_usecase import MiddleUseCase, DBOperations


class InsertCustomShortURLUseCase(MiddleUseCase):
    def __init__(self, repository: DBOperations):
        super().__init__(repository)

    async def execute(self, original_url: str, short_url: str | None) -> ShortURLBase:
        return await self.insert_url(original_url, short_url)
