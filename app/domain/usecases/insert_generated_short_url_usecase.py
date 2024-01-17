from random import choices
from string import ascii_uppercase, ascii_lowercase, digits

from .middle_usecase import MiddleUseCase, DBOperations


class InsertGeneratedURLUseCase(MiddleUseCase):
    def __init__(self, repository: DBOperations):
        super().__init__(repository)

    async def execute(self, original_url: str, short_url: str | None = None):
        generated_short_url = ''.join(choices(ascii_uppercase + ascii_lowercase + digits, k=15))
        return await self.insert_url(original_url, generated_short_url)
