from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def post_confirm_markup():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ Ha", callback_data="confirm_post"),
        InlineKeyboardButton("❌ Yo‘q", callback_data="cancel_post")
    )
    return markup