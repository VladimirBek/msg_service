from fastapi import Depends

from app.message.application.repositories.message_repository_impl import MessageRepositoryImpl
from app.message.application.usecases.create import CreateMessageUseCaseImpl

from app.message.application.usecases.get_list import GetMessagesUseCaseImpl


def get_message_repository():
    return MessageRepositoryImpl()


def get_messages_usecase(message_repository=Depends(get_message_repository)):
    return GetMessagesUseCaseImpl(message_repository)


def get_create_message_usecase(message_repository=Depends(get_message_repository)):
    return CreateMessageUseCaseImpl(message_repository)
