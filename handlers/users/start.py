from aiogram import types
from loader import dp
from utils.db_api.users import get_user
from states.register import RegisterState
from aiogram.dispatcher import FSMContext
from keyboards.default.user import user_menu
from keyboards.default.admin import admin_menu
from utils.env_tools import get_admin_ids  # ✅ .env’dan admin ID’larni olish

@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # ✅ Agar admin bo‘lsa – admin menyu ko‘rsatilsin
    if user_id in get_admin_ids():
        await message.answer("👋 Salom Admin! Menyu quyidagicha:", reply_markup=admin_menu)
        return

    # ✅ Oddiy foydalanuvchi bo‘lsa – ro‘yxatdan o‘tganmi tekshir
    user = get_user(user_id)
    if user:
        await message.answer("👋 Assalomu alaykum!", reply_markup=user_menu)
    else:
        await message.answer("🔐 Botdan foydalanish uchun ro'yxatdan o'ting.\n\nIsm va familiyangizni kiriting:")
        await RegisterState.full_name.set()