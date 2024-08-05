from fastapi import HTTPException, Depends

from app.message.dependencies import get_create_message_usecase
from app.message.domain.models.message_model import MessageCreateModel, MessageReadModel
from app.message.domain.usecases.create import CreateMessageUseCase
from app.message.presentation.api.routes import router


@router.post("/",
             response_model=MessageReadModel,
             status_code=201)
async def create_message(message_create_model: MessageCreateModel,
                         message_create_usecase: CreateMessageUseCase = Depends(get_create_message_usecase)) -> MessageReadModel:
    try:
        new_message = await message_create_usecase((message_create_model,))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    return new_message
