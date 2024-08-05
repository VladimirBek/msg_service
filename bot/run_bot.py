import asyncio

from bot import BotServiceHandlers

if __name__ == '__main__':
    bot = BotServiceHandlers()
    asyncio.run(bot.start_bot())
