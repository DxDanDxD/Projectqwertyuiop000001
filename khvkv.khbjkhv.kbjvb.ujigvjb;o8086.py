import random
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message,state: FSMContext):
    reply_keyboard = [['6', '7', '8', '9', '10']]
    await message.reply('Добро пожаловать в игру "Мафия"! Выберите количество игроков:',
                        reply_markup=types.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    await state.set_state('s1')


@dp.message_handler(lambda message: message.text.isdigit(), state='s1')
async def select_players(message: types.Message,state: FSMContext):
    num_players: message
    mafia_count: int
    villagers_count: int
    if num_players==6:
        mafia_count==2
        villagers_count==4

    if num_players==7:
        mafia_count==2
        villagers_count==5
    if num_players==8:
        mafia_count==3
        villagers_count==5
    if num_players==9:
        mafia_count==3
        villagers_count==6
    if num_players==10:
        mafia_count==3
        villagers_count==7
    await message.reply(f'Игра началась! В игре {num_players} игроков: {mafia_count} мафиози и {villagers_count} мирных жителей.')
    await state.set_state('s2')


executor.start_polling(dp, skip_updates=True)
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
