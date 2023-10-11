from typing import Callable, Awaitable, Dict, Any
import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

class DbSession(BaseMiddleware):
    def __init__(self):
        pass