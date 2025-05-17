from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu=ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Birinchi tugma"),
        KeyboardButton(text="Ikkinchi tugma")
    ],
    [
        KeyboardButton(text="Uchinchi tugma")
    ]
]
,resize_keyboard=True)