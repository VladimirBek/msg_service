from app.message.application.errors.message_errors import MessagesNotFoundError
from app.message.dependencies import get_messages_usecase
from app.message.domain.models.message_model import MessageReadModel
from app.message.domain.usecases.get_list import GetMessagesUseCase
from app.message.presentation.api.routes import router
from fastapi import status, Depends, HTTPException

from app.message.presentation.api.schemas.error_messages import ErrorMessageMessagesNotFound


@router.get("/",
            response_model=list[MessageReadModel],
            status_code=200,
            responses={
                status.HTTP_404_NOT_FOUND: {
                    'model': ErrorMessageMessagesNotFound
                }
            })
async def get_list(skip: int = 0, limit: int = 100,
                   message_usecase: GetMessagesUseCase = Depends(get_messages_usecase)) -> \
        list[MessageReadModel]:
    try:
        return await message_usecase((limit, skip))
    except MessagesNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
