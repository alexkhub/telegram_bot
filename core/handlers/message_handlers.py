from aiogram import Bot, F
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
from core.utils.machine_condition import Steps_New_Link
from aiogram.fsm.context import FSMContext
from core.utils.models import *


async def user_start_bot(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=f"Добрый день {message.from_user.full_name}",
                           reply_markup=reply_keyboard)


async def call_back(message: Message, bot: Bot) -> None:
    await bot.send_message(chat_id=message.from_user.id, text=f"привет, id ={message.from_user.id}")


async def create_new_link(message: Message, state: FSMContext) -> None:
    await message.answer(f'{message.from_user.full_name}, введите название')
    await state.set_state(Steps_New_Link.GET_LINK_NAME)


async def get_link_name(message: Message, state: FSMContext) -> None:
    await message.answer(f' ссылка "{message.text}", теперь введите ссылку')
    await state.update_data(link=message.text)
    await state.set_state(Steps_New_Link.GET_LINK)


async def get_link(message: Message, state: FSMContext) -> None:
    await message.answer(f'названиме "{message.text}", теперь укажите категорию')
    await state.update_data(name=message.text)
    await state.set_state(Steps_New_Link.SELECT_CATEGORY)


async def select_category(message: Message, state: FSMContext) -> None:
    await message.answer(f'вы создали ссылку')
    context_data = await  state.get_data()
    link = context_data.get('link')
    name = context_data.get('name')
    category = message.text

    await state.clear()
