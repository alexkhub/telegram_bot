from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='регистрация'
        ),
        KeyboardButton(
            text='посмотреть статьи'
        )
    ],
    [
        KeyboardButton(
            text='категории'
        ),
        KeyboardButton(
            text='поиск'
        )
    ]
]
)
