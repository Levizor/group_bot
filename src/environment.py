from dotenv import load_dotenv
import os

load_dotenv()

def get_bot_token() -> str:
    bot_token = os.getenv("BOT_TOKEN")
    if bot_token is None:
        raise Exception("No bot token defined in .env")

    return bot_token

def get_yt_dir() -> str | None:
    return os.getenv("YT_DIR")

def get_bot_username() -> str:
    return os.getenv("BOT_USERNAME") or "BOTYARA"
