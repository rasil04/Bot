from aiogram import types


async def check_words(message: types.Message):
    """
    Функция для отлавливания плохих слов
    """
    bad_words = ["говно", "залупа", "пенис", "хер", "давалка", "хуй", "блядина",
                 "головка", "шлюха", "жопа", "член", "еблан", "петух", "мудила",
                 "рукоблуд", "ссанина", "очко", "блядун", "вагина",
                 "сука", "ебланище", "влагалище", "пердун", "дрочила",
                 "пизда", "туз", "малафья", "гомик", "мудила", "пилотка", "манда",
                 "анус", "вагина", "путана", "педрила", "шалава", "хуила", "мошонка", "елда"]
    if message.chat.type != 'private':
        for word in bad_words:
            if word in message.text.lower().replace(' ', ''):
                await message.reply(text=f' Пользователь {message.from_user.first_name} отправил запрещенное слово \n'
                                         f'Админы забанить {message.from_user.first_name}: Да\Нет')
                break




async def check_user_is_admin(message: types.Message):
    """
    Функция для проверки прав админа автора сообщения
    в том чате, в который сообщение было отправлено
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
    return False


async def yes_no(message: types.Message):
    """
    Функция обрабатывает ответы администраторов беседы и банит пользователя
    """
    if message.chat.type != 'private':
        answer_admin = await check_user_is_admin(message)
        print(answer_admin)
        if answer_admin and message.reply_to_message:
            # await message.reply(message.reply_to_message.from_user.username)
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )