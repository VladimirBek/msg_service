import json

from beanie import Link
from redis import asyncio as aioredis
from bson import ObjectId

from app.message.application.models.message import Message
from app.message.domain.models.message_model import MessageReadModel
from app.user.application.models.user import User
import json
from datetime import datetime


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class RedisService:
    def __init__(self, redis: aioredis.Redis) -> None:
        self._redis = redis

    async def cache_message(self, message: Message):

        message_dict = message.dict()
        message_dict['id'] = str(message_dict['id'])
        if isinstance(message.user, User):
            print(message.user.dict())
            message_dict['user'] = message.user.dict()
        elif isinstance(message.user, Link):
            user = await message.user.fetch()
            message_dict['user'] = user.dict()

        message_dict['user']['id'] = str(message_dict['user']['id'])

        await self._redis.set(str(message.id), json.dumps(message_dict, cls=CustomJSONEncoder))

    async def get_cached_message(self, message_id: ObjectId) -> MessageReadModel | None:
        cached_data = await self._redis.get(str(message_id))
        if cached_data:
            message_dict = json.loads(cached_data)
            message_dict['id'] = ObjectId(message_dict['id'])
            message_dict['user']['id'] = ObjectId(message_dict['user']['id'])
            return MessageReadModel(**message_dict)
        return None

    async def get_all_cached_messages(self) -> list[MessageReadModel]:
        messages = []
        async for key in self._redis.scan_iter("*"):
            cached_data = await self._redis.get(key)
            if cached_data:
                message_dict = json.loads(cached_data)
                message_dict['id'] = ObjectId(message_dict['id'])
                message_dict['user']['id'] = ObjectId(message_dict['user']['id'])
                message_dict['created_at'] = datetime.fromisoformat(message_dict['created_at'])
                messages.append(MessageReadModel(**message_dict))
        return messages

    async def clean(self) -> None:
        await self._redis.flushall()
