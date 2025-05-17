import logging

from aiogram import Bot
from data.config import ADMINS

async def on_startup_notify(bot: Bot):
        for admin in ADMINS:
            try:
                await bot.send_message(admin, "Hey admin, I'm working!")
            except Exception as err:
                logging.exception(err)
