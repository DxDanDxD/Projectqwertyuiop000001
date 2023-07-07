from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Привет, как тебя зовут?")
    await state.set_state("name")


@dp.message_handler(state="age")
async def age_handler(message: types.Message, state: FSMContext):
    await message.answer("Эта функция никогда не вызовется")


@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer(f"{name}, добро пожаловать в эхо бота!")
    await state.set_state("echo")


@dp.message_handler(state="echo")
async def echo_nadler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'{user_data["name"]} сказал: {message.text}')


executor.start_polling(dp, skip_updates=True)