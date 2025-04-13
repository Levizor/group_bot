from aiogram.filters import Filter
from aiogram.types.message import Message


class ContainsBotNameFilter(Filter):
    def __init__(self, name: str):
        self.name = name

    async def __call__(self, message: Message) -> bool:
        if message.text is None:
            return False
        return self.name in message.text
