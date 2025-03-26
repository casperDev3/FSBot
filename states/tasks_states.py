from aiogram.fsm.state import StatesGroup, State

class Tasks(StatesGroup):
    title = State()
    description = State()
    link = State()