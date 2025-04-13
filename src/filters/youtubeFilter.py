from aiogram.filters import Filter
from aiogram.types.message import Message
import re

class YoutubeLinkFilter(Filter):


    YOUTUBE_REGEX = re.compile(
        r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌[\w\?‌=]*)?'  # Match URLs containing "youtube"
    )
    
    async def __call__(self, message: Message) -> bool:
        if message.text is None: 
            return False
        if not YoutubeLinkFilter.YOUTUBE_REGEX.match(message.text):
            return False

        return True



