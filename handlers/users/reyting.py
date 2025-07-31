from aiogram import types
from loader import dp
from keyboards.default.reyting import reyting_menu
from keyboards.default.user import user_menu

@dp.message_handler(text="📊 Reyting")
async def show_reyting_menu(message: types.Message):
    await message.answer("📊 Reyting bo‘limi:", reply_markup=reyting_menu)

@dp.message_handler(text="⬅️ Orqaga")
async def back_from_reyting(message: types.Message):
    await message.answer("🔙 Asosiy menyuga qaytdingiz.", reply_markup=user_menu)