from datetime import datetime
from uuid import uuid4, UUID

from beanie import Document, Link
from pydantic import Field

from app.user.application.models.user import User


class Message(Document):
    user: Link[User]
    text: str
    created_at: datetime
