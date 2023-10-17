from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='запуск бота'

        ),
        BotCommand(
            command='help',
            description='помощь'
        ),
        BotCommand(
            command='new_link',
            description='новая ссылка'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
