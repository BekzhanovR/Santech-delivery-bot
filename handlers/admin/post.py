from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.post import PostState
from keyboards.inline.post_confirm import post_confirm_markup
from keyboards.default.post import orqaga_menu
from keyboards.default.admin import admin_menu
from utils.db_api.users import get_all_user_ids


@dp.message_handler(text="✏️ Post yuborish")
async def start_post(message: types.Message):
    await message.answer("📝 Post matnini yuboring:", reply_markup=orqaga_menu)
    await PostState.text.set()


@dp.message_handler(lambda m: m.text == "⬅️ Orqaga qaytish", state=PostState.text)
@dp.message_handler(lambda m: m.text == "⬅️ Orqaga qaytish", state=PostState.media)
async def cancel_post_reply(message: types.Message, state: FSMContext):
    await message.answer("❌ Post yuborish bekor qilindi.", reply_markup=admin_menu)
    await state.finish()


@dp.message_handler(content_types=types.ContentType.TEXT, state=PostState.text)
async def get_post_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("📎 Endi rasm yoki video yuboring (yoki '⬅️ Orqaga qaytish')", reply_markup=orqaga_menu)
    await PostState.media.set()


@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.TEXT], state=PostState.media)
async def get_post_media(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    media_type = message.content_type

    await state.update_data(media_type=media_type)

    if media_type == "photo":
        file_id = message.photo[-1].file_id
        await state.update_data(media_id=file_id)
        await message.answer_photo(file_id, caption=text, reply_markup=post_confirm_markup())
    elif media_type == "video":
        file_id = message.video.file_id
        await state.update_data(media_id=file_id)
        await message.answer_video(file_id, caption=text, reply_markup=post_confirm_markup())
    else:
        await message.answer(text, reply_markup=post_confirm_markup())

    await PostState.confirm.set()


@dp.callback_query_handler(text="confirm_post", state=PostState.confirm)
async def confirm_post(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    media_id = data.get("media_id")
    media_type = data.get("media_type")
    count = 0

    for user_id in get_all_user_ids():
        try:
            if media_type == "photo":
                await bot.send_photo(user_id, media_id, caption=text)
            elif media_type == "video":
                await bot.send_video(user_id, media_id, caption=text)
            else:
                await bot.send_message(user_id, text)
            count += 1
        except:
            continue

    await callback.message.edit_text(f"✅ Post {count} ta foydalanuvchiga yuborildi.")
    await state.finish()


@dp.callback_query_handler(text="cancel_post", state=PostState.confirm)
async def cancel_post_confirm(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("❌ Post yuborish bekor qilindi.")
    await state.finish()