from typing import Tuple

from app.user.application.errors.user_errors import UserAlreadyExistsError
from app.user.application.repositories.user_repository_impl import UserRepositoryImpl
from app.user.domain.models.user_model import UserCreateModel, UserReadModel
from app.user.domain.usecases.create import CreateUserUsecase


class CreateUserUsecaseImpl(CreateUserUsecase):
    def __init__(self, user_repository):
        self.user_repository: UserRepositoryImpl = user_repository

    async def __call__(self, args: Tuple[UserCreateModel]):
        data, = args
        if await self.user_repository.get_by_tg_id(data.tg_id):
            raise UserAlreadyExistsError()
        new_user = await self.user_repository.create(data.to_document())
        return UserReadModel.from_document(new_user)
