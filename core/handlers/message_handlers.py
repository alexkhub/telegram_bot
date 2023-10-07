from aiogram import Bot, F
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
from main import dp


async def user_start_bot(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=f"Добрый день {message.from_user.full_name}", reply_markup=reply_keyboard)


async def call_back(message: Message, bot: Bot) -> None:
    await bot.send_message(chat_id=message.from_user.id, text=f"привет, id ={message.from_user.id}")
