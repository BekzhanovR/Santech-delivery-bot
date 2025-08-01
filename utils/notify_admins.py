from aiogram import Dispatcher
from utils.env_tools import get_admin_ids
import logging

async def on_startup_notify(dp: Dispatcher):
    try:
        for admin_id in get_admin_ids():
            await dp.bot.send_message(admin_id, "✅ Bot ishga tushdi!")
    except Exception as err:
        logging.exception(err)