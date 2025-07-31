from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📊 Statistikani olish")],
        [KeyboardButton("👥 Kasblar")],
        [
            KeyboardButton("⭐ Obuna sozlamalari"),
            KeyboardButton("✏️ Post yuborish")
        ],
        [KeyboardButton("📣 Kanal sozlamalari")],
        [KeyboardButton("🛠 Xodimlar qo‘shish")],
        [KeyboardButton("⚙️ Sozlamalar")],
    ],
    resize_keyboard=True
)