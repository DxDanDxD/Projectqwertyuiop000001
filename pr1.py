from __future__ import annotations

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

b1 = KeyboardButton("чат 1 на 1")
b2 = KeyboardButton("групповой чат")

choose_chat_type_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True).insert(b1).insert(b2)

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Добро пожаловать в чат-рулетку! Как тебя зовут?')
    await state.set_state('name')


@dp.message_handler(state='name')
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.reply(f'Приятно познакомиться {name}! Как ты  хочешь общаться?',
                        reply_markup=choose_chat_type_keyboard)
    await state.set_state('ready')


@dp.message_handler(commands='find', state='ready')
async def find_handler(message: types.Message, state: FSMContext):
    await message.answer('Ищем собеседника...')
    waiting_users.add(message.from_user.id)
    print(message.from_user.username)
    while len(waiting_users) >= 2:
        user_1_id = waiting_users.pop()
        user_2_id = waiting_users.pop()

        await dp.current_state(chat=user_1_id, user=user_1_id).set_state('chatting')
        await dp.current_state(chat=user_2_id, user=user_2_id).set_state('chatting')
        # TODO: посмотреть всё ли нормально

        connected_pairs[user_1_id] = user_2_id
        connected_pairs[user_2_id] = user_1_id

        await bot.send_message(chat_id=user_1_id, text='Вы начали общаться')
        await bot.send_message(chat_id=user_2_id, text='Вы начали общаться')


executor.start_polling(dp, skip_updates=True)