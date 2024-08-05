from pydantic import BaseModel, Field

from app.message.application.errors.message_errors import MessagesNotFoundError


class ErrorMessageMessagesNotFound(BaseModel):
    detail: str = Field(example=MessagesNotFoundError.message)
