from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    load_dotenv()
    MONGODB_DB: str
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str

    BOT_TOKEN: str
    MONGODB_DSN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
