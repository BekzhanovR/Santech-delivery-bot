from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📝 Ariza yuborish")],
        [KeyboardButton("💼 Ish kerak"), KeyboardButton("🧑‍💼 Ishshi kerak")],
        [KeyboardButton("⭐ Premium obuna"), KeyboardButton("📣 Reklama berish")],
        [KeyboardButton("📊 Reyting")],
        [KeyboardButton("💻 ADMIN ga murojaat qilish")],
        [KeyboardButton("⚙️ Sozlamalar")],
    ],
    resize_keyboard=True
)