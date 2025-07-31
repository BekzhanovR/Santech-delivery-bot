import logging
from aiogram import Dispatcher
from data.config import ADMINS

async def on_startup_notify(dp: Dispatcher):
    for admin_id in ADMINS:
        try:
            await dp.bot.send_message(admin_id, "✅ Bot muvaffaqiyatli ishga tushdi!")
        except Exception as err:
            logging.exception(f"❌ Adminga habar yuborishda xatolik: {admin_id} — {err}")