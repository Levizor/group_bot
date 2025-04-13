
from aiogram import Router, flags
from aiogram.types import InputFileUnion, message, FSInputFile, Message
from aiogram.utils.chat_action import ChatActionMiddleware

from filters import YoutubeLinkFilter
from .ytdownloader import DownloadedVideo, YTDownloader


youtubeRouter = Router()
youtubeRouter.message.middleware(ChatActionMiddleware())
downloader = YTDownloader()

@youtubeRouter.message(YoutubeLinkFilter())
@flags.chat_action("upload_video")
async def showInfo(message: Message):
    assert isinstance(message.text, str), "Must be str"
    link: str = message.text

    try:
        video: DownloadedVideo = await downloader.download(link)
        file = FSInputFile(video.get_path())

        await message.reply_video(file)
        video.delete()
    except Exception as e:
        await message.reply(f"Error occured while trying to download a video")



