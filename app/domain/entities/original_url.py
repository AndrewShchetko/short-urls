from pydantic import BaseModel, Field, HttpUrl


class OriginalURLBase(BaseModel):
    long_url: HttpUrl = Field(examples=["https://fastapi.tiangolo.com/learn/"])
