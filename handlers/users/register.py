from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.register import RegisterState
from utils.db_api.users import add_user
from keyboards.default.user import user_menu

@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)

    contact_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    contact_kb.add(types.KeyboardButton("📱 Raqam yuborish", request_contact=True))

    await message.answer("📲 Endi telefon raqamingizni yuboring:", reply_markup=contact_kb)
    await RegisterState.next()  # <--- MUHIM! Bu `phone` holatiga o‘tadi

@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterState.phone)
async def get_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    data = await state.get_data()
    full_name = data.get("full_name")
    user_id = message.from_user.id

    add_user(user_id, full_name, phone)

    await message.answer("✅ Ro'yxatdan o'tdingiz!", reply_markup=user_menu)
    await state.finish()