from datetime import datetime
from typing import Optional, Annotated
from uuid import UUID

from bson import ObjectId
from pydantic import BaseModel

from app.core.value_objects.object_id_pydantic import ObjectIdPydanticAnnotation
from app.user.application.models.user import User


class BaseUser(BaseModel):
    pass


class UserReadModel(BaseUser):
    id: UUID
    tg_id: int
    first_name: str
    last_name: str | None
    username: str | None
    created_at: datetime

    @staticmethod
    def from_document(document):
        return UserReadModel(
            id=document.id,
            tg_id=document.tg_id,
            first_name=document.first_name,
            last_name=document.last_name,
            username=document.username,
            created_at=document.created_at
        )

    class Config:
        arbitrary_types_allowed = True


class UserCreateModel(BaseUser):
    tg_id: int
    first_name: str
    last_name: str | None
    username: str | None
    created_at: datetime = datetime.now()

    def to_document(self):
        return User(tg_id=self.tg_id, first_name=self.first_name, last_name=self.last_name,
                    username=self.username, created_at=self.created_at)


class UserUpdateModel(BaseUser):
    id: UUID | None = None
    tg_id: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    created_at: datetime | None = None

    class Config:
        arbitrary_types_allowed = True
