from app.core.repositories.mongo_repository import MongoRepository
from app.user.application.models.user import User


class UserRepositoryImpl(MongoRepository):

    collection = User

    async def get_by_tg_id(self, tg_id: int) -> User:
        return await self.collection.find_one({"tg_id": tg_id})

