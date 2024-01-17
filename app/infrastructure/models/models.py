from typing import List

from sqlalchemy import String, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()


class OriginalURL(Base):
    __tablename__ = "original_urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    long_url: Mapped[str] = mapped_column(String(255))

    short_urls: Mapped[List["ShortURL"]] = relationship(back_populates="long_url", cascade="all, delete-orphan")

    UniqueConstraint("long_url")

    def __repr__(self) -> str:
        return f"OriginalURL(id: {self.id}, long url: {self.long_url}, short_urls: {self.short_urls})"


class ShortURL(Base):
    __tablename__ = "short_urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str] = mapped_column(String(15))
    long_url_id: Mapped[int] = mapped_column(ForeignKey("original_urls.id"))

    long_url: Mapped["OriginalURL"] = relationship(back_populates='short_urls', lazy="joined")

    UniqueConstraint("short_url", "long_url_id")

    def __repr__(self) -> str:
        return f"ShortURL(id: {self.id}, long url: {self.short_url}, long_url_id: {self.long_url_id})"
