import asyncio
from aiogram import Bot, html
from aiogram.client.default import DefaultBotProperties
from os import getenv
from aiogram.enums import ParseMode

TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def send_10_sec_notification(userId, message):
    await bot.send_message(chat_id=userId, text=message)

async def scheduler():
    while True:
        await send_10_sec_notification(1387518953, "Hello, World!")
        await asyncio.sleep(30)  # wait for 30 seconds before sending the next message

asyncio.run(scheduler())
