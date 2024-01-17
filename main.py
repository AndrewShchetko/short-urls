from fastapi import FastAPI

from app.infrastructure.api.v0.create_url_router import post_router
from app.infrastructure.api.v0.get_url_router import get_router

app = FastAPI()

app.include_router(get_router)
app.include_router(post_router)
