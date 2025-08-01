from aiogram.dispatcher.filters.state import StatesGroup, State

class AdminAddState(StatesGroup):
    get_id = State()