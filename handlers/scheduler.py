from aiogram.types import Message
from config import scheduler, bot


async def handler_scheduler(message: Message):
    """
        Функция напоминалка
    """
    text = message.text[8:]
    chat_id = message.from_user.id
    scheduler.add_job(job_handler, 'cron', seconds=10, args=(text, chat_id))
    await message.answer(text="Понял, принял и напомнил!")


async def job_handler(text, chat_id):
    print('ok')
    await bot.send_message(
        chat_id=chat_id,
        text=text
    )