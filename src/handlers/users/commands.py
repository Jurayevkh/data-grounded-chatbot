from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command,CommandStart

import database.requests as request
from database.requests import set_user


commands_router=Router()

@commands_router.message(CommandStart())
async def start_command(message: Message):
    await request.set_user(message.from_user.id)
    await message.reply("<b>Salom botga xush kelibsiz</b>")

@commands_router.message(Command("help"))
async def help_command(message: Message):
    text=("🔹<b>Doira Bot sizga qanday yordam beradi?</b> \n"
          "✅ Haftalik tadbirlar, master-klasslar va treninglar haqida ma’lumot olish.\n"
          "✅ O‘z yutuqlaringiz va sertifikatlaringizni saqlab, tadbirlarga tez va oson ro'yxatdan o'ting.\n"
          "✅ Do‘stlar va boshqa ishtirokchilar bilan bog‘lanish va netvorking yaratish.\n\n"
          "🌐<b>Netvorking doirangizni biz bilan kengaytiring!</b>")
    await message.reply(text)