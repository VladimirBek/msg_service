from app.core.repositories.mongo_repository import MongoRepository
from app.message.application.models.message import Message


class MessageRepositoryImpl(MongoRepository):

    collection = Message

