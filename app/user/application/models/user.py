from datetime import datetime

from beanie import Document


class User(Document):
    tg_id: int | None
    first_name: str
    last_name: str | None
    username: str | None
    created_at: datetime