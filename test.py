import asyncio

from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import Settings


class Sample(Document):
    name: str

async def init():
    settings = Settings()
    # Create Motor client
    client = AsyncIOMotorClient(
        settings.MONGODB_DSN
    )

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client.db_name, document_models=[Sample])

async def main():
    await init()
    sample = Sample(name="test")
    await sample.create()
    print(sample)

asyncio.run(main())
