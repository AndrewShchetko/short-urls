from pydantic import BaseSettings


class PostgresSettings(BaseSettings):
    name: str
    user: str
    password: str
    host: str
    port: str

    class Config:
        env_prefix = "db_"
