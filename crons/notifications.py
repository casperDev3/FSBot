import asyncio
from aiogram import Bot, html
from aiogram.client.default import DefaultBotProperties
from os import getenv
from aiogram.enums import ParseMode
import schedule
import time

TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# async def main():
#     await bot.send_message(chat_id=1387518953, text=f"Hello, {html.bold('World')}!")

async def send_10_sec_notification(userId, message):
    await bot.send_message(chat_id=userId, text=f"{message}")

# asyncio.run(main())
