from typing import Tuple

from beanie import Link

from app.message.application.repositories.message_repository_impl import MessageRepositoryImpl
from app.message.domain.models.message_model import MessageReadModel
from app.message.domain.usecases.get_list import GetMessagesUseCase
from app.user.domain.entity.user import UserEntity


class GetMessagesUseCaseImpl(GetMessagesUseCase):

    def __init__(self, message_repository: MessageRepositoryImpl):
        self.message_repository = message_repository

    async def __call__(self, args: Tuple[int, int]) -> list[MessageReadModel]:
        limit, offset = args
        message_documents = await self.message_repository.findall(limit, offset)
        return [await MessageReadModel.from_document(message) for message in message_documents]
