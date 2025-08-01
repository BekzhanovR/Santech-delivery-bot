from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

xodimlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🙍‍♂️ ADMIN qo‘shish"),
            KeyboardButton("📞 OPERATOR qo‘shish")
        ],
        [KeyboardButton("⬅️ Orqaga qaytish")]
    ],
    resize_keyboard=True
)