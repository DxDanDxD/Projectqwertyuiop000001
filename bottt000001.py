from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """Ловец - обработчик сообщений"""
    await message.answer("Добро пожаловать в тестовый бот.")


@dp.message_handler(content_types=['text'])
async def start_handler(message: types.Message):
    await message.answer(message.text)


"""@dp.message_handler(content_types=['text'])
async def start_handler(message: types.Message):
    await bot.send_message(message.text)"""


executor.start_polling(dp, skip_updates=True)
