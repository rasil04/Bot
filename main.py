import random

from aiogram import Bot, Dispatcher, executor, types
import logging
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def hello(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}!")

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer('''
/start - Начало работы с ботом
/help - Список команд
/myinfo - Информация вашего профиля
/picture - Отправить рандомную пикчу
    ''')

@dp.message_handler(commands=["myinfo"])
async def info_sender(message: types.Message):
    await message.answer(f'''
Ваше имя: {message.from_user.first_name}
Ваш ID: {message.from_id}
    ''')

@dp.message_handler(commands=["picture"])
async def image_sender(message: types.Message):
    await message.answer_photo(open(f'./images/' + random.choice(os.listdir('images')), 'rb'))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)