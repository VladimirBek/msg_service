from datetime import datetime

from beanie import Document
from pydantic import BaseModel

from app.user.application.models.user import User


class UserEntity(BaseModel):
    tg_id: int | None
    first_name: str
    last_name: str | None
    username: str | None
    created_at: datetime

    def to_document(self):
        return User(tg_id=self.tg_id, first_name=self.first_name, last_name=self.last_name,
                    username=self.username, created_at=self.created_at)
    @staticmethod
    def from_document(document):
        return UserEntity(tg_id=document.tg_id, first_name=document.first_name, last_name=document.last_name,
                          username=document.username, created_at=document.created_at)

    def __eq__(self, other):
        if not isinstance(other, UserEntity):
            return NotImplemented
        return self.id_ == other.id_
