import pydantic
from fastapi import APIRouter

from app.domain.entities.short_url import ShortURLBase
from app.domain.usecases.insert_custom_short_url_usecase import InsertCustomShortURLUseCase
from app.domain.usecases.insert_generated_short_url_usecase import InsertGeneratedURLUseCase
from app.infrastructure.repositories.postgresql.url_repository import URLRepository

post_router = APIRouter(
    prefix="/create"
)


@post_router.post("/generate_short_url", response_model=ShortURLBase)
async def create_generated_short_url(
        long_url: pydantic.HttpUrl = "https://fastapi.tiangolo.com/learn/"
) -> ShortURLBase:
    use_case = InsertGeneratedURLUseCase(URLRepository())
    return await use_case.execute(long_url)


@post_router.post("/custom_short_url", response_model=ShortURLBase)
async def create_custom_short_url(
        long_url: pydantic.HttpUrl = "https://fastapi.tiangolo.com/learn/",
        short_url: str = "fastapi"
) -> ShortURLBase:
    use_case = InsertCustomShortURLUseCase(URLRepository())
    return await use_case.execute(long_url, short_url)
