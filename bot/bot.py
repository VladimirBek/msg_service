from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import SimpleEventIsolation, MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

from app.config import Settings
from handlers.user import UserHandler


class BotServiceHandlers:
    __slots__ = "dp", "bot", "config"
    user_commands = [
        BotCommand(command="start", description="Старт / главное меню"),
        BotCommand(command="show_messages", description="Показать все сообщения")
    ]

    def __init__(self):
        # инициализируем root-бота и диспатчер
        self.config = Settings()
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage, events_isolation=SimpleEventIsolation())
        self.dp = dp
        bot = Bot(token=self.config.BOT_TOKEN)
        self.bot = bot
        UserHandler(self.dp).register_handlers()

    async def start_bot(self):
        """Start bot polling / set webhook"""
        await self.bot.set_my_commands(self.user_commands, scope=BotCommandScopeDefault())
        await self.dp.start_polling(self.bot, settings=self.config)
