from datetime import datetime
from typing import Optional, Annotated
from uuid import UUID, uuid4

from beanie import Document, Link
from bson import ObjectId
from pydantic import BaseModel

from app.core.value_objects.object_id_pydantic import ObjectIdPydanticAnnotation
from app.message.application.models.message import Message
from app.user.application.models.user import User
from app.user.domain.entity.user import UserEntity


class BaseMessage(BaseModel):
    pass


class MessageReadModel(BaseMessage):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation]
    user: User
    text: str
    created_at: datetime

    @staticmethod
    async def from_document(document):
        if isinstance(document.user, User):
            return MessageReadModel(
                id=document.id,
                user=document.user,
                text=document.text,
                created_at=document.created_at
            )
        elif isinstance(document.user, Link):
            user_model = await document.user.fetch()
            return MessageReadModel(
                id=document.id,
                user=user_model,
                text=document.text,
                created_at=document.created_at
            )
    class Config:
        arbitrary_types_allowed = True


class MessageCreateModel(BaseMessage):
    user: UserEntity
    text: str
    created_at: datetime = datetime.now()

    def to_document(self):
        return Message(**self.model_dump(mode='json'))


class MessageUpdateModel(BaseMessage):
    id: UUID | None = None
    user: UserEntity | None = None
    text: str | None = None
    created_at: datetime | None = None
