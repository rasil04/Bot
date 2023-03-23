from aiogram import types
import random
import os


async def start(message: types.Message):
    """
    Команда start - Начало работы с ботом
    """
    await message.answer(f"Привет {message.from_user.first_name}!")

async def help(message: types.Message):
    """
    Команда help - Выводит базовые команды бота
    """
    await message.answer('''
/start - Начало работы с ботом
/help - Список команд
/myinfo - Информация вашего профиля
/picture - Отправить рандомную пикчу
    ''')

async def my_info(message: types.Message):
    """
    Команда myinfo - Выдает пользователю информацию об его аккаунте
    """
    await message.answer(f'''
Ваше имя: {message.from_user.first_name}
Ваш ID: {message.from_id}
    ''')

async def random_picture(message: types.Message):
    """
    Команда picture - Отправляет пользователю рандрмную картинку из папки images
    """
    await message.answer_photo(open(f'./images/' + random.choice(os.listdir('images')), 'rb'))