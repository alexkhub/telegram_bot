from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


categories_keyboard = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='регистрация'
            ),
            InlineKeyboardButton(
                text='посмотреть статьи'
            )
        ],
        [
            InlineKeyboardButton(
                text='категории'
            ),
            InlineKeyboardButton(
                text='поиск'
            )
        ]
    ]
)