from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.admins import AdminAddState
from utils.env_tools import append_admin_id_to_env
from keyboards.default.xodimlar import xodimlar_menu
from keyboards.default.admin import admin_menu
from keyboards.default.common import orqaga_button

@dp.message_handler(text="🛠 Xodimlar qo‘shish")
async def show_xodimlar_menu(message: types.Message):
    await message.answer("🧑‍💼 Xodimlar qo‘shish bo‘limi:", reply_markup=xodimlar_menu)

@dp.message_handler(text="⬅️ Orqaga qaytish")
async def back_from_xodimlar(message: types.Message):
    await message.answer("🔙 Admin menyusiga qaytdingiz.", reply_markup=admin_menu)

@dp.message_handler(text="🙍‍♂️ ADMIN qo‘shish")
async def ask_new_admin_id(message: types.Message):
    await message.answer(
        "🆔 Yangi adminning Telegram ID sini yuboring:",
        reply_markup=orqaga_button
    )
    await AdminAddState.get_id.set()

@dp.message_handler(lambda msg: msg.text == "⬅️ Orqaga qaytish", state=AdminAddState.get_id)
async def cancel_admin_add(message: types.Message, state: FSMContext):
    await message.answer("❌ Admin qo‘shish bekor qilindi.", reply_markup=xodimlar_menu)
    await state.finish()

@dp.message_handler(state=AdminAddState.get_id)
async def save_new_admin_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Iltimos, faqat raqam kiriting!")
        return

    new_id = int(message.text)
    result = append_admin_id_to_env(new_id)

    if result:
        await message.answer(f"✅ {new_id} ID admin sifatida muvaffaqiyatli qo‘shildi!", reply_markup=admin_menu)
    else:
        await message.answer("⚠️ Bu ID allaqachon mavjud yoki xatolik yuz berdi.", reply_markup=admin_menu)

    await state.finish()