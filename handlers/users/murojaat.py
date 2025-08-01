from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from states.murojaat import MurojaatState
from keyboards.default.murojaat import murojaat_confirm_menu
from keyboards.default.user import user_menu

@dp.message_handler(text="💻 ADMIN ga murojaat qilish")
async def ask_question(message: types.Message):
    await message.answer("✍️ Matnli murojaatingizni yozib qoldiring:")
    await MurojaatState.input_text.set()

@dp.message_handler(state=MurojaatState.input_text)
async def receive_question(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("✅ Murojaatingizni yuborish uchun tasdiqlang:", reply_markup=murojaat_confirm_menu)
    await MurojaatState.confirm.set()

@dp.message_handler(lambda msg: msg.text == "✅ Murojaat yuborish", state=MurojaatState.confirm)
async def send_to_admin(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")

    for admin_id in ADMINS:
        try:
            await bot.send_message(
                admin_id,
                f"📩 <b>Yangi murojaat</b>\n\n<b>Foydalanuvchi:</b> {message.from_user.full_name} (@{message.from_user.username})\n<b>ID:</b> {message.from_user.id}\n\n📝 {text}",
                parse_mode="HTML"
            )
        except:
            continue

    await message.answer("✅ Murojaatingiz yuborildi!", reply_markup=user_menu)
    await state.finish()

@dp.message_handler(lambda msg: msg.text in ["❌ Bekor qilish", "⬅️ Orqaga qaytish"], state=MurojaatState.confirm)
async def cancel_murojaat(message: types.Message, state: FSMContext):
    await message.answer("❌ Murojaat yuborish bekor qilindi.", reply_markup=user_menu)
    await state.finish()