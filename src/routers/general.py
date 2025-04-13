from aiogram import Bot, Router
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types.message import Message

from environment import get_bot_username
from filters.containsBotName import ContainsBotNameFilter
from filters.isReplyMessage import IsReplyMessage


generalRouter = Router()

@generalRouter.message(CommandStart())
async def start(message: Message):
    message.answer("Hello there")
    await help(message)

@generalRouter.message(Command("help"))
async def help(message: Message):
    message.reply("Send youtube video link and I will download it")

@generalRouter.message(ContainsBotNameFilter(get_bot_username()), IsReplyMessage())
async def redirect(message: Message, dispatcher: Dispatcher, bot: Bot):
    assert isinstance(message.reply_to_message, Message)
    msg = message.reply_to_message.model_copy(update={"COMMAND": True, "from_user": message.from_user})
    await dispatcher.feed_raw_update(bot=bot, update={"update_id": 3, "message": msg})
