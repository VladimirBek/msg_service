from app.user.application.errors.user_errors import UserAlreadyExistsError
from app.user.dependencies import get_create_user_usecase
from app.user.domain.models.user_model import UserReadModel, UserCreateModel
from app.user.presentation.api.routes import router
from fastapi import status, Depends, HTTPException


@router.post('/', response_model=UserReadModel, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreateModel,
    user_create_usecase=Depends(get_create_user_usecase)
):
    try:
        new_user = user_create_usecase(user)
    except UserAlreadyExistsError:
        raise HTTPException(status.HTTP_409_CONFLICT, detail='User already exists')

    return new_user
