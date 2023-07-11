from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

active_users: set[int] = set()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    active_users.add(message.from_user.id)
    await message.answer("Добро пожаловать в комнату!")


@dp.message_handler()
async def chatting_handler(message: types.Message):
    for id in active_users:
        bot.send_message(chat_id=id, text=message.text)

executor.start_polling(dp, skip_updates=True)