
from abc import abstractmethod
from typing import Tuple

from app.core.usecase.base_usecase import BaseUseCase
from app.user.domain.models.user_model import UserReadModel, UserCreateModel


class CreateUserUsecase(BaseUseCase[Tuple[UserCreateModel], UserReadModel]):

    @abstractmethod
    async def __call__(self, args: Tuple[UserCreateModel]) -> UserReadModel:
        raise NotImplementedError()
