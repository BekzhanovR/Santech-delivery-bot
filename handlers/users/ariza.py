from aiogram import types
from loader import dp
from keyboards.default.ariza import ariza_menu
from keyboards.default.user import user_menu

@dp.message_handler(text="📝 Ariza yuborish")
async def show_ariza_menu(message: types.Message):
    await message.answer("🗂 Kerakli turdagi arizani tanlang:", reply_markup=ariza_menu)

@dp.message_handler(text="⬅️ Orqaga")
async def back_to_main_menu(message: types.Message):
    await message.answer("🔙 Asosiy menyuga qaytdingiz.", reply_markup=user_menu)