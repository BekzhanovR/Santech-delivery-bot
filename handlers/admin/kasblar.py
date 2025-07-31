from aiogram import types
from loader import dp
from utils.db_api.kasblar import get_all_kasblar, delete_kasb
from keyboards.inline.kasblar import kasblar_menu_with_pagination,  kasblar_inline_markup
from keyboards.default.kasblar import kasblar_menu
from aiogram.dispatcher import FSMContext
from states.kasb import KasbState
from utils.db_api.kasblar import add_kasb

@dp.message_handler(text="👥 Kasblar")
async def show_kasblar_menu(message: types.Message):
    await message.answer("👥 Kasblar bo‘limi:", reply_markup=kasblar_menu)

@dp.message_handler(text="⬅️ Orqaga qaytish")
async def back_to_admin_from_kasblar(message: types.Message):
    await message.answer("🔙 Admin menyusiga qaytdingiz.", reply_markup=admin_menu)


@dp.message_handler(text="👁 Kasblarni ko‘rish")
async def show_kasblar(message: types.Message, state: FSMContext):
    kasblar = get_all_kasblar()
    if not kasblar:
        await message.answer("❗️Hozircha kasblar yo‘q", reply_markup=kasblar_menu)
        return
    await state.update_data(kasblar_page=1)
    markup = kasblar_menu_with_pagination(kasblar, page=1)
    await message.answer("📄 Kasblar ro‘yxati:", reply_markup=markup)

@dp.message_handler(text="➡️ Keyingi sahifa")
async def next_page_kasblar(message: types.Message, state: FSMContext):
    kasblar = get_all_kasblar()
    state_data = await state.get_data()
    current_page = state_data.get("kasblar_page", 1)
    new_page = current_page + 1
    await state.update_data(kasblar_page=new_page)
    markup = kasblar_menu_with_pagination(kasblar, page=new_page)
    await message.answer("📄 Keyingi sahifa:", reply_markup=markup)

@dp.message_handler(text="⬅️ Oldingi sahifa")
async def prev_page_kasblar(message: types.Message, state: FSMContext):
    kasblar = get_all_kasblar()
    state_data = await state.get_data()
    current_page = state_data.get("kasblar_page", 1)
    new_page = max(current_page - 1, 1)
    await state.update_data(kasblar_page=new_page)
    markup = kasblar_menu_with_pagination(kasblar, page=new_page)
    await message.answer("📄 Oldingi sahifa:", reply_markup=markup)

@dp.message_handler(text="➕ Kasb qo‘shish")
async def ask_kasb_name(message: types.Message):
    await message.answer("✍️ Iltimos, qo‘shmoqchi bo‘lgan kasb nomini kiriting:")
    await KasbState.add_name.set()

@dp.message_handler(state=KasbState.add_name)
async def save_kasb_name(message: types.Message, state: FSMContext):
    kasb_nomi = message.text.strip()

    if not kasb_nomi:
        await message.answer("⚠️ Kasb nomi bo‘sh bo‘lishi mumkin emas.")
        return

    success = add_kasb(kasb_nomi)
    if success:
        await message.answer(f"✅ '{kasb_nomi}' kasbi muvaffaqiyatli qo‘shildi.")
    else:
        await message.answer("❌ Bu kasb allaqachon mavjud yoki xatolik yuz berdi.")

    await state.finish()

@dp.message_handler(text="➖ Kasb o‘chirish")
async def delete_kasb_menu(message: types.Message):
    kasblar = get_all_kasblar()
    if not kasblar:
        await message.answer("❗️Hozircha o‘chirish uchun kasblar yo‘q.")
        return

    markup = kasblar_inline_markup(kasblar)
    await message.answer("🗑 O‘chirmoqchi bo‘lgan kasbni tanlang:", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data.startswith("del_kasb:"))
async def confirm_delete_kasb(callback: types.CallbackQuery):
    kasb_nomi = callback.data.split(":")[1]

    if delete_kasb(kasb_nomi):
        await callback.message.edit_text(f"✅ '{kasb_nomi}' kasbi o‘chirildi.")
    else:
        await callback.message.edit_text("❌ Xatolik: kasb o‘chirilmadi.")