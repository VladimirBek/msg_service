from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from app.config import Settings
from app.core.repositories.base_repository import BaseRepository


class MongoRepository(BaseRepository):
    collection = None

    def __init__(self, connection: AsyncIOMotorClient, db_name: str = Settings().MONGODB_DB):
        self.connection = connection
        self.database = connection.get_database(db_name)

    async def create(self, entity: BaseModel):
        await self.database[self.collection].insert_one(entity.dict())

    async def findall(self, limit=1000, offset=None):
        cursor = self.database[self.collection].find(limit=limit, skip=offset)
        return await cursor.to_list(length=limit)

    async def find_by_id(self, id_: int):
        return await self.database[self.collection].find_one({"_id": id_})

    async def update(self, entity: BaseModel):
        await self.database[self.collection].update_one({"_id": entity.id}, {"$set": entity.dict()})

    async def delete_by_id(self, id_: int):
        await self.database[self.collection].delete_one({"_id": id_})
