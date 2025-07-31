from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from math import ceil

def kasblar_menu_with_pagination(kasblar: list, page: int = 1, per_page: int = 10) -> ReplyKeyboardMarkup:
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    start = (page - 1) * per_page
    end = start + per_page
    current_page_kasblar = kasblar[start:end]

    for i in range(0, len(current_page_kasblar), 2):
        row = current_page_kasblar[i:i+2]
        buttons = [KeyboardButton(kasb) for kasb in row]
        menu.row(*buttons)

    total_pages = ceil(len(kasblar) / per_page)

    nav_buttons = []
    if page > 1:
        nav_buttons.append(KeyboardButton("⬅️ Oldingi sahifa"))
    if page < total_pages:
        nav_buttons.append(KeyboardButton("➡️ Keyingi sahifa"))

    if nav_buttons:
        menu.row(*nav_buttons)

    menu.add(KeyboardButton("⬅️ Orqaga qaytish"))
    return menu

def kasblar_inline_markup(kasblar: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    for kasb in kasblar:
        markup.insert(InlineKeyboardButton(text=kasb, callback_data=f"del_kasb:{kasb}"))
    return markup