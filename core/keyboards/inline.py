from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


categories_keyboard = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='django',
                callback_data='django'
            ),
            InlineKeyboardButton(
                text='python',
                callback_data='python'
            )
        ],
        # [
        #     InlineKeyboardButton(
        #         text='категории'
        #     ),
        #     InlineKeyboardButton(
        #         text='поиск'
        #     )
        # ]
    ]
)