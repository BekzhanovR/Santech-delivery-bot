from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ariza_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🧑‍🎓 Ish qidiruvchi"),
            KeyboardButton("🧑‍💼 Ish beruvchi")
        ],
        [KeyboardButton("⬅️ Orqaga")]
    ],
    resize_keyboard=True
)