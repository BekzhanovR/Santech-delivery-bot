from aiogram import types
from loader import dp
from keyboards.default.user import user_menu

@dp.message_handler(text="💼 Ish kerak")
async def show_ariza_menu(message: types.Message):
    await message.answer("🕔 Tez kunda qoshiladi!")

@dp.message_handler(text="🧑‍💼 Ishshi kerak")
async def show_ariza_menu(message: types.Message):
    await message.answer("🕔 Tez kunda qoshiladi!")
