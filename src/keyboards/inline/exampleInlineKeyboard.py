from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

optionEvent=InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(text="Birinchi tugma", callback_data="first_keyboard"),
    InlineKeyboardButton(text="Ikkinchi tugma", callback_data="second_keyboard")
    ],
    [InlineKeyboardButton(text="Uchinchi tugma", callback_data="third_keyboard")]
])