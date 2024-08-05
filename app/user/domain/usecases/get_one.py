from abc import abstractmethod
from typing import Tuple

from app.core.usecase.base_usecase import BaseUseCase
from app.user.domain.models.user_model import UserReadModel


class GetUserUsecase(BaseUseCase[Tuple[int], UserReadModel]):

    @abstractmethod
    async def __call__(self, args: Tuple[int]) -> UserReadModel:
        raise NotImplementedError()