from fastapi import Depends

from app.user.application.repositories.user_repository_impl import UserRepositoryImpl
from app.user.application.usecases.create import CreateUserUsecaseImpl
from app.user.application.usecases.get_one import GetUserUsecaseImpl
from app.user.domain.usecases.create import CreateUserUsecase
from app.user.domain.usecases.get_one import GetUserUsecase


def get_user_repository():
    return UserRepositoryImpl()


def get_user_usecase(user_repository: UserRepositoryImpl = Depends(get_user_repository)) -> GetUserUsecase:
    return GetUserUsecaseImpl(user_repository=user_repository)


def get_create_user_usecase(user_repository: UserRepositoryImpl = Depends(get_user_repository)) -> CreateUserUsecase:
    return CreateUserUsecaseImpl(user_repository=user_repository)
