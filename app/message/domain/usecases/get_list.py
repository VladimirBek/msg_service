from abc import abstractmethod
from typing import Tuple

from app.core.usecase.base_usecase import BaseUseCase
from app.message.domain.models.message_model import MessageReadModel


class GetMessagesUseCase(BaseUseCase[Tuple[int, int], list[MessageReadModel]]):

    @abstractmethod
    async def __call__(self, args: Tuple[int, int]) -> list[MessageReadModel]:
        raise NotImplementedError()
