from typing import Optional

from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    load_dotenv()
    MONGODB_DB: str
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str

    BOT_TOKEN: str
    MONGODB_DSN: Optional[str] = None

    REDIS_HOST: str

    @field_validator("MONGODB_DSN")
    @classmethod
    def validate_mongodb_dsn(cls, v: Optional[str], info: FieldValidationInfo):
        if isinstance(v, str):
            return v
        user = info.data.get("MONGODB_USER")
        password = info.data.get("MONGODB_PASSWORD")
        host = info.data.get("MONGODB_HOST")
        db = info.data.get("MONGODB_DB")
        port = info.data.get("MONGODB_PORT")
        if not user:
            raise ValueError("MONGODB_USER is required")
        if not password:
            raise ValueError("MONGODB_PASSWORD is required")
        if not host:
            raise ValueError("MONGODB_HOST is required")
        if not db:
            raise ValueError("MONGODB_DB is required")
        if not port:
            raise ValueError("MONGODB_PORT is required")

        return f"mongodb://{user}:{password}@{host}:{port}/{db}?authSource=admin&retryWrites=true&w=majority"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
