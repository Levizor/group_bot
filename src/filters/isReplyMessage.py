
from aiogram.filters.base import Filter
from aiogram.types import Message


class IsReplyMessage(Filter):
    
    async def __call__(self, message: Message):
        if message.reply_to_message is not None:
            return True
        return False
    
