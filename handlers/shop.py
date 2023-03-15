from aiogram import types

kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("Аксессуары"), types.KeyboardButton("Мышки")
)
kb.add(
    types.KeyboardButton("Адрес")
)

async def show_categories(message: types.Message):
    """Функция показывает категории товаров"""
    await message.reply("Наши товары", reply_markup=kb)


async def show_category_accessories(message: types.Message):
    """Функция показывает категорию 'Аксессуары'"""
    kb_accessories = types.InlineKeyboardMarkup()
    kb_accessories.add(
        types.InlineKeyboardButton(text="Наушники", url="https://row.hyperx.com/ru/collections/gaming-headsets/products/hyperx-cloud-stinger?variant=40853229437133"),
        types.InlineKeyboardButton(text="Коврик", callback_data="pass")
    )
    await message.answer("Аксессуары:", reply_markup=kb_accessories)


async def show_category_mouses(message: types.Message):
    """Функция показывает категорию 'Мышки'"""
    await message.answer("Мышки:", reply_markup=kb)


async def show_adress(message: types.Message):
    """Функция показывающая адрес"""
    await message.answer("Чуй 42")