from typing import AsyncIterator

from redis import asyncio as aioredis
from fastapi import Depends

from app.config import Settings
from app.core.redis.redis_service import RedisService
from app.message.application.repositories.message_repository_impl import MessageRepositoryImpl
from app.message.application.usecases.create import CreateMessageUseCaseImpl

from app.message.application.usecases.get_list import GetMessagesUseCaseImpl

async def get_redis() -> AsyncIterator[aioredis.Redis]:
    session = aioredis.from_url(f"redis://{Settings().REDIS_HOST}", encoding="utf-8", decode_responses=True)
    redis_service = RedisService(session)
    yield redis_service
    await redis_service._redis.close()

def get_message_repository():
    return MessageRepositoryImpl()


def get_messages_usecase(message_repository=Depends(get_message_repository),
                         redis=Depends(get_redis)):
    return GetMessagesUseCaseImpl(message_repository, redis)


def get_create_message_usecase(message_repository=Depends(get_message_repository), redis=Depends(get_redis)):
    return CreateMessageUseCaseImpl(message_repository, redis)
