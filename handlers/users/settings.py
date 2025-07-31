from aiogram import types
from loader import dp
from keyboards.default.settings import settings_menu
from keyboards.default.user import user_menu

@dp.message_handler(text="⚙️ Sozlamalar")
async def show_settings(message: types.Message):
    await message.answer("⚙️ Sozlamalar menyusi:", reply_markup=settings_menu)

@dp.message_handler(text="⬅️ Orqaga")
async def back_from_settings(message: types.Message):
    await message.answer("🔙 Asosiy menyuga qaytdingiz.", reply_markup=user_menu)
