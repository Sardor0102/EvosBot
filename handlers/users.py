from utils.loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.reply_btn import main_menu, foods_menu_btn, leave_feedback_btn, settings_text_btn, language_list_btn


@dp.message_handler(commands=['start', 's'])
async def start_command(message: Message):
    btn = await main_menu()
    await message.answer("Выберите одно из следующих", reply_markup=btn)


@dp.message_handler(text="🍴 Меню")
async def foods_menu(message: Message):
    btn = await foods_menu_btn()
    await message.answer("Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=btn)


@dp.message_handler(text="🗺 Мои адреса")
async def my_locations(message: Message):
    await message.answer("Пусто")


@dp.message_handler(text="⬅️ Назад")
async def back_to_main_menu(message: Message):
    await start_command(message)


@dp.message_handler(text="🛍 Мои заказы")
async def my_orders(message: Message):
    await message.answer("Вы совсем ничего не заказали.")


@dp.message_handler(text="✍️ Оставить отзыв")
async def send_comment(message: Message):
    btn = await leave_feedback_btn()
    await message.answer("Поделитесь контактом для дальнейшего связи с Вами", reply_markup=btn)


@dp.message_handler(text="⚙️ Настройки")
async def settings_text(message: Message):
    btn = await settings_text_btn()
    await message.answer("Выберите действие:", reply_markup=btn)


@dp.message_handler(text="Изменить язык")
async def set_language(message: Message):
    btn = await language_list_btn()
    await message.answer("Выберите действие:", reply_markup=btn)


@dp.message_handler(text=['🇷🇺 Русский', '🇺🇿 O\'zbekcha'])
async def set_language(message: Message):
    btn = await main_menu()
    await message.answer("✅ Готово", reply_markup=btn)








