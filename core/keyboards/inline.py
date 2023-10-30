from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kb = [
        [KeyboardButton(text="С пюрешкой")],
        [KeyboardButton(text="Без пюрешки")]
    ]
categories_keyboard = ReplyKeyboardMarkup(keyboard=kb)
