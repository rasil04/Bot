from aiogram.types import Message
from config import scheduler, bot


async def handler_scheduler(message: Message):
    """
        Функция напоминалка
    """
    global reminder
    global chat_id
    reminder = message.text[8:]
    chat_id = message.from_user.id
    scheduler.add_job(job_handler, 'interval', seconds=10, args=(chat_id,))
    await message.answer("Понял, принял и напомнил!")


async def job_handler(chat_id):
    await bot.send_message(
        chat_id=chat_id,
        text=reminder
    )