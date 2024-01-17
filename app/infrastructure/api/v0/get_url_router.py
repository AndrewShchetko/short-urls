from fastapi import APIRouter
from app.domain.usecases.get_original_url_usecase import GetOriginalURLUseCase
from app.domain.entities.original_url import OriginalURLBase
from app.infrastructure.repositories.postgresql.url_repository import URLRepository


get_router = APIRouter()


@get_router.get("/urls/{url_name}", response_model=OriginalURLBase)
async def get_url(url_name: str):
    use_case = GetOriginalURLUseCase(URLRepository())
    return await use_case.execute(url_name)
