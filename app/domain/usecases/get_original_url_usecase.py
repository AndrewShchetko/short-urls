from .base_usecase import BaseUseCase
from app.domain.interfaces.db import DBOperations


class GetOriginalURLUseCase(BaseUseCase):
    def __init__(self, repository: DBOperations):
        self.repository = repository

    async def execute(self, short_url: str):
        async with self.repository as repo:
            orig_url_obj = await repo.get_original_url(short_url)
            return orig_url_obj
