from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reyting_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📊 Ishchilar reytingi"),
            KeyboardButton("📊 Ish beruvchilar reytingi")
        ],
        [KeyboardButton("🙍‍♂️ Mening reytingim")],
        [KeyboardButton("⬅️ Orqaga")]
    ],
    resize_keyboard=True
)