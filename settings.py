from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_DB_URL: str
    DB: str
    book_collection: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
