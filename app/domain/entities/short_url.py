from pydantic import BaseModel, Field


class ShortURLBase(BaseModel):
    short_url: str | None = Field(default="", examples=[""])
