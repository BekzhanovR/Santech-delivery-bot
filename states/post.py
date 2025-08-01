from aiogram.dispatcher.filters.state import StatesGroup, State

class PostState(StatesGroup):
    text = State()
    media = State()
    confirm = State()