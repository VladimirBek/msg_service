from typing import Tuple

from beanie.odm.queries.find import FindMany

from app.message.application.repositories.message_repository_impl import MessageRepositoryImpl
from app.message.domain.models.message_model import MessageReadModel, MessageCreateModel
from app.message.domain.usecases.create import CreateMessageUseCase
from app.user.application.models.user import User


class CreateMessageUseCaseImpl(CreateMessageUseCase):

    def __init__(self, message_repository: MessageRepositoryImpl):
        self.message_repository = message_repository

    async def __call__(self, args: Tuple[MessageCreateModel]) -> MessageReadModel:
        data, = args
        user_document = await User.find({"tg_id": data.user.tg_id}).to_list()
        if not user_document:
            user_document = [data.user.to_document()]
        data = data.to_document()
        data.user = user_document[0]
        message_document = await self.message_repository.create(data)
        return await MessageReadModel.from_document(message_document)

