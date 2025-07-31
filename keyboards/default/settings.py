from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🙍‍♂️ Profil")],
        [
            KeyboardButton("💼 Portfolio qo‘shish"),
            KeyboardButton("🇺🇿 uz Tilni sozlash")
        ],
        [KeyboardButton("⬅️ Orqaga")]
    ],
    resize_keyboard=True
)