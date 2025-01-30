from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = "7913141290:AAFH3uUIp0iqMIL1Yn3dHUQPpO00LJ0DWB0"

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from api import create_user
from handlers.user_private import router

dp = Dispatcher()

ALLOWED_UPDATES=['message', 'edited_message']

dp.include_router(router)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())