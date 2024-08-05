from abc import abstractmethod
from typing import Tuple

from app.core.usecase.base_usecase import BaseUseCase
from app.message.domain.models.message_model import MessageReadModel, MessageCreateModel


class CreateMessageUseCase(BaseUseCase[Tuple[MessageCreateModel], MessageReadModel]):

    @abstractmethod
    async def __call__(self, args: Tuple[MessageCreateModel]) -> MessageReadModel:
        raise NotImplementedError()
