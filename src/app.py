import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import routers_list
from aiogram.client.bot import DefaultBotProperties

from data import config
from utils.set_commands import set_bot_commands
from utils.notify_admins import on_startup_notify
from database.models import async_main

bot=Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML,link_preview_is_disabled=True))
dp=Dispatcher()

async def on_startup():
    await async_main()
    await set_bot_commands(bot)
    await on_startup_notify(bot)
    dp.include_routers(*routers_list)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(on_startup())

