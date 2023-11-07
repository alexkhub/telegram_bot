import asyncio
import logging

import sys

from aiogram import Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from core.utils.machine_condition import Steps_New_Link

# from core.settings import settings
from core.config import *
from core.handlers.message_handlers import *
from core.utils.commands import *
from core.keyboards.reply import *
from core.handlers.callback_query_handler import *

dp = Dispatcher()


@dp.startup()
async def start_bot(bot: Bot) -> None:
    await set_commands(bot)

    await bot.send_message(chat_id=ADMIN_TOKEN, text='Бот запущен')


@dp.shutdown()
async def stop_bot(bot: Bot) -> None:
    await bot.send_message(chat_id=ADMIN_TOKEN, text='Бот приостановлен')


async def main() -> None:
    bot = Bot(TOKEN_API, parse_mode=ParseMode.HTML)

    dp.message.register(user_start_bot, Command(commands=['start', 'run']))  # активация при запуске
    dp.message.register(create_new_link, Command(commands='new_link'))
    dp.message.register(register_user, Command(commands='registration'))
    dp.message.register(get_category, Command(commands='check_categories'))
    dp.message.register(get_help, Command(commands='get_help'))
    dp.message.register(get_link_name, Steps_New_Link.GET_LINK_NAME)
    dp.message.register(get_link, Steps_New_Link.GET_LINK)
    dp.message.register(select_category, Steps_New_Link.SELECT_CATEGORY)
    dp.message.register(call_back, F.text == 'привет')
    dp.message.register(register_user, F.text == 'регистрация')
    dp.callback_query.register(vote_collback)
    try:

        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
