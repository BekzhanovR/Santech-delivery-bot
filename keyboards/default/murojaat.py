from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

murojaat_confirm_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("✅ Murojaat yuborish"),
            KeyboardButton("❌ Bekor qilish")
        ],
        [KeyboardButton("⬅️ Orqaga qaytish")]
    ],
    resize_keyboard=True
)