from aiogram import Bot, F
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
from core.utils.machine_condition import Steps_New_Link
from aiogram.fsm.context import FSMContext


async def user_start_bot(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=f"Добрый день {message.from_user.full_name}",
                           reply_markup=reply_keyboard)


async def call_back(message: Message, bot: Bot) -> None:
    await bot.send_message(chat_id=message.from_user.id, text=f"привет, id ={message.from_user.id}")


async def create_new_link(message: Message, state: FSMContext) -> None:
    await message.answer(f'{message.from_user.full_name}, введите ссылку')
    await state.set_state(Steps_New_Link.GET_LINK_NAME)


async def get_link(message: Message) -> None:
    await message.answer(f' ссылка {message.text}, теперь введите название', )
