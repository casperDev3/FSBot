from aiogram.fsm.state import StatesGroup, State

class SearchEmployeeByName(StatesGroup):
    query = State()