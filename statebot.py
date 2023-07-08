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



@dp.message_handler(commands=['start'], state='name')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Сколько тебе лет?")
    await state.set_state("age")


@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer(f"{name}, добро пожаловать в эхо бота!")
    await state.set_state("echo")



@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    if name=='Julia' or name=='Юля' or name=='Юлия':
        await message.answer("Привет от Дани!")
    await state.update_data({"name": name})
    await message.answer(f"{name}, добро пожаловать в эхо бота!")
    await state.set_state("echo")


@dp.message_handler(state="echo")
async def echo_nadler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'{user_data["name"]} сказал: {message.text}')

@dp.message_handler(commands=['help'], state='*')
async def start_handler(message: types.Message):
    await message.answer("Этот бот повторяет за вами всё, что вы говорите. Чтобы начать пользоваться ботом, напишите /start.")


executor.start_polling(dp, skip_updates=True)