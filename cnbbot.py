from config import TOKEN
import time
import random
from random import randint
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

number: int
ecount = 0

@dp.message_handler(commands=['help'], state='*')
async def helper(message: types.Message, state: FSMContext):
    await message.answer('"COWS AND BULLS" is a game of guessing.'
                         'The system creates number which consists of non-repeating digits.')
    time.sleep(0.5)
    await message.answer(' Your goal is to guess this number.'
                         'If your guess includes digit that is present in the system`s number and is not located on the place you placed it, then it`s called "COW"')
    time.sleep(0.5)
    await message.answer('If your guess includes digit that is present in the system`s number and is indeed located on the place you put it on, then it`s called "BULL"')

    time.sleep(0.5)
    await message.answer('Please, don`t waste your time tryna break the bot by entering text, that will work not.')

    if state==(2):
        time.sleep(0.5)
        await message.answer('Now that you know the rules, stick to guessing.')
    else:
        time.sleep(0.5)
        await message.answer('Shall we /start ?')
    await state.set_state('2')

@dp.message_handler(commands=['start'],state='*')
async def start_game(message: types.Message, state: FSMContext):
    await message.answer('Welcome to the game "COWS AND BULLS"!')
    time.sleep(0.5)
    await message.answer('The game has begun.')
    time.sleep(0.5)
    await message.answer('Type your guess:')
    """x1 = randint(0, 9)
    x10 = randint(0, 9)
    x100 = randint(0, 9)
    x1000 = randint(1, 9)
    if x10 == x1 or x10 == x100 or x10 == x1000:
        x10 = randint(0, 9)
    if x100 == x1 or x100 == x10 or x100 == x1000:
        x100 = randint(0, 9)
    if x1000 == x1 or x10 == x100 or x10 == x10:
        x1000 = randint(1, 9)"""
    global number
    digits = list(range(10))
    random.shuffle(digits)
    global number
    number = int(''.join(map(str, digits[:4])))
    #number = x1 + x10 * 10 + x100 * 100 + x1000 * 1000

    #await message.answer(number)
    await state.set_state(2)

@dp.message_handler(commands=['restart'],state='restart')
async def start_game(message: types.Message, state: FSMContext):
    """x1 = randint(0, 9)
    x10 = randint(0, 9)
    x100 = randint(0, 9)
    x1000 = randint(1, 9)
    if x10 == x1 or x10 == x100 or x10 == x1000:
        x10 = randint(0, 9)
    if x100 == x1 or x100 == x10 or x100 == x1000:
        x100 = randint(0, 9)
    if x1000 == x1 or x10 == x100 or x10 == x10:
        x1000 = randint(1, 9)"""
    await message.answer('Type your guess:')
    global number
    digits = list(range(10))
    random.shuffle(digits)
    global number
    number = int(''.join(map(str, digits[:4])))
    #number = x1 + x10 * 10 + x100 * 100 + x1000 * 1000

    #await message.answer(number)
    await state.set_state(2)

@dp.message_handler(state='2')
async def process_guess(message: types.Message, state: FSMContext):

    """await state.update_data(number=number)
    data = await state.get_data()
    number = data['number']"""

    if message.text.isdigit():
        guess = int(message.text)

        if guess == 2903:
            await message.answer(number)

        ones = guess % 10
        decs = ((guess - guess % 10) / 10) % 10
        cents = ((guess - guess % 100) / 100) % 10
        mills = ((guess - guess % 1000) / 1000) % 10

        if guess != number:
            cows = 0
            bulls = 0

            if ones == number // 10 % 10 or ones == number // 100 % 10 or ones == number // 1000:
                cows += 1
            if ones == number % 10:
                bulls += 1

            if decs == number % 10 or decs == number // 100 % 10 or decs == number // 1000:
                cows += 1
            if decs == number // 10 % 10:
                bulls += 1

            if cents == number // 10 % 10 or cents == number % 10 or cents == number // 1000:
                cows += 1
            if cents == number // 100:
                bulls += 1

            if mills == number // 10 % 10 or mills == number // 100 % 10 or mills == number % 10:
                cows += 1
            if mills == number // 1000:
                bulls += 1

            await message.answer(f'Bulls: {bulls}, Cows: {cows}')

        else:
            await message.answer('Congratulations! You guessed!')
            await message.answer('/restart to start again.')
            await state.set_state('restart')
    else:

        global ecount
        if ecount == 4:
            ecount-=4
            await state.reset_state()
            await message.answer('I told ya not to try... Didn`t I? Now... look what have you done!!!')
        else:
            await message.answer('Ooops... This doesn"t look like number. Try again!')
            ecount+=1
            await state.set_state('2')

executor.start_polling(dp, skip_updates=True)