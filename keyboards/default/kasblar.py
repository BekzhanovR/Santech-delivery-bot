from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kasblar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("👁 Kasblarni ko‘rish")],
        [
            KeyboardButton("➕ Kasb qo‘shish"),
            KeyboardButton("➖ Kasb o‘chirish")
        ],
        [KeyboardButton("⬅️ Orqaga qaytish")]
    ],
    resize_keyboard=True
)
