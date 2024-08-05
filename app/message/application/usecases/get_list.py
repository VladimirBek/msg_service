from typing import Tuple

from app.core.redis.redis_service import RedisService
from app.message.application.errors.message_errors import MessagesNotFoundError
from app.message.application.repositories.message_repository_impl import MessageRepositoryImpl
from app.message.domain.models.message_model import MessageReadModel
from app.message.domain.usecases.get_list import GetMessagesUseCase


class GetMessagesUseCaseImpl(GetMessagesUseCase):

    def __init__(self, message_repository: MessageRepositoryImpl, redis: RedisService):
        self.message_repository = message_repository
        self.redis = redis

    async def __call__(self, args: Tuple[int, int]) -> list[MessageReadModel]:
        limit, offset = args
        all_messages_in_redis = await self.redis.get_all_cached_messages()
        message_documents = await self.message_repository.findall(limit, offset)
        if not message_documents and not all_messages_in_redis:
            raise MessagesNotFoundError()
        if len(all_messages_in_redis) != len(message_documents):
            return [await MessageReadModel.from_document(message) for message in message_documents]
        else:
            return all_messages_in_redis
