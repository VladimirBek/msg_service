import asyncio

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import Settings
from app.message.application.models.message import Message
from app.user.application.models.user import User

models = [Message, User]


async def initiate_database():
    config = Settings()
    client = AsyncIOMotorClient(config.MONGODB_DSN)
    await init_beanie(
        database=client.db_name, document_models=models
    )
