from aiogram import types
from loader import dp
from keyboards.default.channel import channel_settings_menu
from keyboards.default.admin import admin_menu

@dp.message_handler(text="📣 Kanal sozlamalari")
async def show_channel_settings(message: types.Message):
    await message.answer("📣 Kanal sozlamalari menyusi:", reply_markup=channel_settings_menu)

@dp.message_handler(text="⬅️ Orqaga qaytish")
async def back_to_admin_menu(message: types.Message):
    await message.answer("🔙 Admin menyusiga qaytdingiz.", reply_markup=admin_menu)