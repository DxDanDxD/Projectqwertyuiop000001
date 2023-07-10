import random
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['5', '6', '7', '8', '9', '10']]
    update.message.reply_text(
        'Добро пожаловать в игру "Мафия"! Выберите количество игроков:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

# Обработчик выбора количества игроков
def select_players(update: Update, context: CallbackContext) -> None:
    num_players = int(update.message.text)
    mafia_count = num_players // 3
    villagers_count = num_players - mafia_count

    # Здесь можно добавить логику распределения ролей и другие правила игры

    update.message.reply_text(f'Игра началась! В игре {num_players} игроков: {mafia_count} мафиози и {villagers_count} мирных жителей.')

# Создаем экземпляр Updater и регистрируем обработчики команд
updater = Updater('TOKEN')
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('select_players', select_players))

# Запускаем бота
updater.start_polling()
updater.idle()