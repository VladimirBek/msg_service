from typing import Tuple

from app.user.application.repositories.user_repository_impl import UserRepositoryImpl
from app.user.domain.models.user_model import UserReadModel
from app.user.domain.usecases.get_one import GetUserUsecase


class GetUserUsecaseImpl(GetUserUsecase):

    def __init__(self, user_repository: UserRepositoryImpl):
        self.user_repository = user_repository

    async def __call__(self, args: Tuple[int]) -> UserReadModel | None:
        user_doc = await self.user_repository.get_by_tg_id(args[0])
        if user_doc is None:
            return None
        return UserReadModel.from_document(user_doc)
