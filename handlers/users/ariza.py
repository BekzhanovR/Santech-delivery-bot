from aiogram import types
from loader import dp
from keyboards.default.ariza import ariza_menu
from keyboards.default.user import user_menu

@dp.message_handler(text="📝 Ariza yuborish")
async def show_ariza_menu(message: types.Message):
    await message.answer("🕔 Tez kunda qoshiladi!")