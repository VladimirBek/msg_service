from app.core.errors.base_error import BaseError


class MessageNotFoundError(BaseError):
    message = 'Message does not exist.'


class MessagesNotFoundError(BaseError):
    message = 'Messages do not exist'

