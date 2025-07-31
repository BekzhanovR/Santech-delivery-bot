from aiogram.dispatcher.filters.state import StatesGroup, State

class KasbState(StatesGroup):
    add_name = State()