from aiogram import Bot, F
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
from core.utils.machine_condition import Steps_New_Link
from aiogram.fsm.context import FSMContext
from core.utils.models import *
from core.utils.database_commands import *
from core.keyboards.inline import categories_keyboard
from core.config import CATEGORIES, HELP_TEXT


async def user_start_bot(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=f"Добрый день {message.from_user.full_name}",
                           reply_markup=reply_keyboard)


async def call_back(message: Message, bot: Bot) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"привет, id ={message.from_user.id, message.contact.phone_number}")


async def register_user(message: Message) -> None:
    user = await register_user_command(message)

    if user:
        await message.answer('Вы успешно зарегистрировались!')
    else:
        await message.answer('Вы уже зарегистрированы!')


# создание ссылки
async def create_new_link(message: Message, state: FSMContext) -> None:
    check = await check_registration(message)
    if check:
        await state.update_data(user_id=check.user_id)
        await message.answer(f'{message.from_user.full_name}, введите название')
        await state.set_state(Steps_New_Link.GET_LINK_NAME)
    else:
        await message.answer(f'вы не зарегистрированы!')


async def get_link_name(message: Message, state: FSMContext) -> None:
    await message.answer(f'название"{message.text}", теперь введите ссылку')
    await state.update_data(name=message.text)
    await state.set_state(Steps_New_Link.GET_LINK)


async def get_link(message: Message, state: FSMContext) -> None:
    await message.answer(f'ссылка "{message.text}", теперь укажите категорию', reply_markup=categories_keyboard)
    await state.update_data(link=message.text)
    await state.set_state(Steps_New_Link.SELECT_CATEGORY)


async def select_category(message: Message, state: FSMContext) -> None:
    await message.answer(f'вы создали ссылку')
    context_data = await state.get_data()
    link = context_data.get('link')
    link_name = context_data.get('name')
    user = context_data.get('user_id')

    category = message.text

    link_obj = await register_list(link=link, link_name=link_name, user=user, category=category)
    if link_obj:
        await message.answer('Ссылка сохранена!')
    else:
        await message.answer('Ошибка сохранения')
    await state.clear()


# конец создания ссылки

async def get_category(message: Message) -> None:
    await message.answer(f'список всех категорий: {CATEGORIES}', )


async def get_help(message: Message) -> None:
    await message.answer(f'{HELP_TEXT}')
