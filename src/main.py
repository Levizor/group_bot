from aiogram import Bot, Dispatcher
from environment import get_bot_token
from routers import *
import asyncio

async def main():
    bot = Bot(get_bot_token())
    dispatcher = createDispatcher()

    print("Polling")
    await dispatcher.start_polling(bot)

def createDispatcher() -> Dispatcher:
    dispatcher = Dispatcher()

    dispatcher.include_routers(generalRouter, youtubeRouter)

    return dispatcher

if __name__ == "__main__":
    asyncio.run(main())
