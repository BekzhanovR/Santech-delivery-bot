from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

obuna_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("👁 POST MATN KO‘RISH")],
        [
            KeyboardButton("✏️ POST YOZISH"),
            KeyboardButton("💸 OBUNA NARXI")
        ],
        [KeyboardButton("⛔ POST o‘chirish")],
        [KeyboardButton("⬅️ Orqaga qaytish")]
    ],
    resize_keyboard=True
)