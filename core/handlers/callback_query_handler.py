
from aiogram.types import Message, CallbackQuery
from core.keyboards.reply import reply_keyboard
from core.utils.machine_condition import Steps_New_Link
from aiogram.fsm.context import FSMContext


from core.keyboards.inline import categories_keyboard
from main import dp


async def category_callback(callback: CallbackQuery):
    if callback.data == 'django':
        return await callback.message.answer("напишите '1' ")
    elif callback.data == 'python':
        return await callback.message.answer("напишите '2' ")
