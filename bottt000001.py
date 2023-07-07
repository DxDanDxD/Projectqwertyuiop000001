"""from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'],state='*')
async def start_handler(message: types.Message,state:FSMContext):
    await message.answer("Добро пожаловать в тестовый бот. Как тебя зовут?")
    await state.set_state("name")


@dp.message_handler(state="age")
async def age_handler(message: types.Message, state: FSMContext):
    await message.answer("nf aeyrwbz ybrjulf yt dspjdtncz")


@dp.message_handler(commands=['start'])
async def name_handler(message: types.Message,state:FSMContext):
    await message.answer("Поздравляю! У тебя стейт name")
    name=message.text\


@dp.message_handler(content_types=['text'])
async def start_handler(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать в тестовый бот.")


@dp.message_handler(content_types=['text'])
async def start_handler(message: types.Message):
    await bot.send_message(message.text)


executor.start_polling(dp, skip_updates=True)"""
