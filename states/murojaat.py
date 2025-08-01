from aiogram.dispatcher.filters.state import State, StatesGroup

class MurojaatState(StatesGroup):
    input_text = State()
    confirm = State()