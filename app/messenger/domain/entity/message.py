from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class MessageEntity(BaseModel):

    id_: UUID
    user_id: UUID
    text: str
    created_at: datetime

    def __eq__(self, other):
        if not isinstance(other, MessageEntity):
            return NotImplemented
        return self.id_ == other.id_


