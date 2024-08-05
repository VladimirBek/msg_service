from fastapi import Depends, HTTPException

from app.message.presentation.api.routes import router
from app.user.dependencies import get_user_usecase
from app.user.domain.models.user_model import UserReadModel


@router.get("/{user_id}", response_model=UserReadModel)
async def get_one(user_id: int, user_usecase=Depends(get_user_usecase)):
    user = await user_usecase((user_id,))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
