from config import TOKEN
from random import randint
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

number=0


@dp.message_handler(commands=['start'],state='*')
async def start_game(message: types.Message, state: FSMContext):
    await message.answer('Welcome to the game of "COWS AND BULLS"!')
    await message.answer('The game has started. Guess now!')
    await message.answer('Type your guess:')

    global number
    x1 = randint(0, 9)
    x10 = randint(0, 9)
    x100 = randint(0, 9)
    x1000 = randint(1, 9)
    if x10 == x1 or x10 == x100 or x10 == x1000:
        x10 = randint(0, 9)
    if x100 == x1 or x100 == x10 or x100 == x1000:
        x100 = randint(0, 9)
    if x1000 == x1 or x10 == x100 or x10 == x10:
        x1000 = randint(1, 9)
    number =number +  x1 + x10 * 10 + x100 * 100 + x1000 * 1000

    #await message.answer(number)
    await state.set_state(2)


@dp.message_handler(state='2')
async def process_guess(message: types.Message, state: FSMContext):

    attempts = 0
    score = 0


    await state.update_data(number=number)
    data = await state.get_data()
    number = data['number']

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
            attempts += 1
        else:
            score += 1
            await message.answer(f'You guessed! Your attempts: {attempts}')
    else:
        await message.answer('Ooops... Try again!')
        errcount += 1
        if errcount == 5:
         await bot.send_message('Stop this! Get some help!')


executor.start_polling(dp, skip_updates=True)