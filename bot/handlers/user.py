import re
from datetime import datetime

import httpx
from aiogram import Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.config import Settings
from app.user.application.models.user import User
from app.user.dependencies import get_user_usecase


class UserHandler:
    __slots__ = "dp", "router"

    host = "web"

    def __init__(self, dp: Dispatcher):
        self.dp = dp
        self.router = Router()
        self.dp.include_router(self.router)

    def register_handlers(self):
        self.router.message.register(self.start, Command('start'))
        self.router.message.register(self.catch_msg, F.text & ~F.text.startswith('/'))
        self.router.message.register(self.show_messages, Command('show_messages'))

    async def catch_msg(self, message: Message):
        async with httpx.AsyncClient() as client:
            message_data = {"text": message.text,
                            "user": {"tg_id": message.from_user.id,
                                     "username": message.from_user.username,
                                     "first_name": message.from_user.first_name,
                                     "last_name": message.from_user.last_name,
                                     "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
                            "created_at": message.date.strftime("%Y-%m-%d %H:%M:%S"),
                            }
            await client.post(f"http://nginx:8080/api/v1/message/", json={**message_data})

    async def start(self, message: Message):
        """ Хэндлер для команды старт """
        await message.answer("Добрый день! В кнопке 'Меню' вы можете выбрать опцию.")

    async def show_messages(self, message: Message):
        """ Хэндлер для команды показать все сообщения """
        async with httpx.AsyncClient() as client:
            messages = await client.get(f"http://nginx:8080/api/v1/message/")
            if messages.status_code != 200:
                await message.answer("Сообщений нет")
                return
        await message.answer("Вот все сообщения:")
        for m in messages.json():
            print(m)
            await message.answer(f"sender: {m['user']['username'], m['user']['first_name'], m['user']['last_name']}\n"
                                 f"{m['text']}\n"
                                 f"{m['created_at']}"
                                 f"\n\n")