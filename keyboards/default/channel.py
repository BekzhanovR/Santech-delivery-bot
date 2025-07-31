from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

channel_settings_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("➕ Kanal qo‘shish"),
            KeyboardButton("➖ Kanal o‘lib tashlash")
        ],
        [KeyboardButton("⬅️ Orqaga qaytish")]
    ],
    resize_keyboard=True
)
