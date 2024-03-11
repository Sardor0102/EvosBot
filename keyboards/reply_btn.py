from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

remove_btn = ReplyKeyboardRemove()


async def main_menu():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn.add(
        KeyboardButton(text="🍴 Меню")
    )

    btn.add(
        KeyboardButton(text="🛍 Мои заказы")
    )

    btn.add(
        KeyboardButton(text="✍️ Оставить отзыв"),
        KeyboardButton(text="⚙️ Настройки")
    )

    return btn


async def foods_menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn.add(
        KeyboardButton(text="🗺 Мои адреса")
    )

    btn.add(
        KeyboardButton(text="Отправить геолокацию", request_location=True),
        KeyboardButton(text="⬅️ Назад")
    )

    return btn


async def leave_feedback_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    btn.add(
        KeyboardButton(text="Phone", request_contact=True),
        KeyboardButton(text="⬅️ Назад")
    )

    return btn


async def settings_text_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    btn.add(
        KeyboardButton(text="Изменить язык"),
        KeyboardButton(text="⬅️ Назад")
    )

    return btn


async def language_list_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn.add(
        KeyboardButton(text="🇷🇺 Русский"),
        KeyboardButton(text="🇺🇿 O'zbekcha"),
        KeyboardButton(text="⬅️ Назад"),
    )

    return btn


