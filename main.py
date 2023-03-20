from aiogram import executor
import logging
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.basic_handlers import (
    start,
    help,
    my_info,
    random_picture
)
from handlers.shop import (
    show_categories,
    show_category_accessories,
    show_category_mouses,
    show_adress
)
from admin.admin import (
    check_words,
    yes_no
)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(show_categories, commands=["start"])
    dp.register_message_handler(show_category_accessories, Text(equals="Аксессуары"))
    dp.register_message_handler(show_category_mouses, Text(equals="Мышки"))
    dp.register_message_handler(show_adress, Text(equals="Адрес"))
    # dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(my_info, commands=["myinfo"])
    dp.register_message_handler(random_picture, commands=["picture"])
    dp.register_message_handler(check_words)
    dp.register_message_handler(yes_no, commands=['Да'], commands_prefix=['!'])
    executor.start_polling(dp)
