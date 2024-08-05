from datetime import datetime
from typing import Annotated
from uuid import UUID

from beanie import Document
from bson import ObjectId
from pydantic import BaseModel

from app.core.value_objects.object_id_pydantic import ObjectIdPydanticAnnotation
from app.message.application.models.message import Message
from app.user.domain.entity.user import UserEntity


class MessageEntity(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation]
    user: UserEntity
    text: str
    created_at: datetime

    def to_document(self):
        return Message(user=self.user, text=self.text, created_at=self.created_at)

    def __eq__(self, other):
        if not isinstance(other, MessageEntity):
            return NotImplemented
        return self.id == other.id
