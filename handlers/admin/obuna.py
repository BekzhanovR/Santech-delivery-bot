from aiogram import types
from loader import dp
from keyboards.default.obuna import obuna_menu
from keyboards.default.admin import admin_menu

@dp.message_handler(text="⭐ Obuna sozlamalari")
async def show_obuna_menu(message: types.Message):
    await message.answer("⭐ Obuna bo‘limi menyusi:", reply_markup=obuna_menu)

@dp.message_handler(text="⬅️ Orqaga qaytish")
async def back_to_admin_from_obuna(message: types.Message):
    await message.answer("🔙 Admin menyusiga qaytdingiz.", reply_markup=admin_menu)