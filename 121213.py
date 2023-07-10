from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Player:
    pnumber: int
    role: str
    status: bool
    def setstatus(self, newstatus:bool):
        self.status=newstatus
    


active_users: set[int] = set()


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    active_users.add(message.from_user.id)
    await message.answer("Привет, как тебя зовут?")
    await state.set_state("name")


@dp.message_handler(state="name")
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer(f"{name}, добро пожаловать в эхо бота!")
    await message.answer("Сколько тебе лет?")
    await state.set_state("peoplequantityselect")


@dp.message_handler(state="peoplequantityselect")
async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data({"age": age})
    await state.set_state("echo")


@dp.message_handler(commands=['help'], state='*')
async def start_handler(message: types.Message):
    await message.answer("Этот бот повторяет за вами всё, что вы говорите. Чтобы начать пользоваться ботом, напишите /start.")


@dp.message_handler(state="echo")
async def echo_nadler(message: types.Message):
    for id in active_users:
       await bot.send_message(chat_id = id , text=message.text)


executor.start_polling(dp, skip_updates=True)