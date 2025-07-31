from aiogram import types
from loader import dp
from data import config
from utils.db_api.users import get_user
from states.register import RegisterState
from aiogram.dispatcher import FSMContext
from keyboards.default.user import user_menu
from keyboards.default.admin import admin_menu

@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # Agar admin bo'lsa — admin menyu
    if user_id in config.ADMINS:
        await message.answer("👋 Salom Admin! Menyu quyidagicha:", reply_markup=admin_menu)
        return

    # Oddiy foydalanuvchi — ro‘yxatdan o‘tganmi?
    user = get_user(user_id)
    if user:
        await message.answer("👋 Assalomu alaykum!", reply_markup=user_menu)
    else:
        await message.answer("🔐 Botdan foydalanish uchun ro'yxatdan o'ting.\n\nIsm va familiyangizni kiriting:")
        await RegisterState.full_name.set()