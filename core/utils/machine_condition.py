from aiogram.fsm.state import State, StatesGroup


class Steps_New_Link(StatesGroup):
    GET_LINK_NAME = State()
