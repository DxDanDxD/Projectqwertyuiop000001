import random
from config import TOKEN
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Создаем экземпляры бота и диспетчера
bot = Bot(token="TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Список для хранения анонимных сообщений
messages = []


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Добро пожаловать в групповой анонимный чат! Введите ваше анонимное сообщение.")


# Обработчик текстовых сообщений
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_message(message: types.Message):
    # Генерируем уникальный идентификатор для анонимного сообщения
    message_id = random.randint(1000, 9999)

    # Добавляем сообщение в список анонимных сообщений
    messages.append({"message_id": message_id, "text": message.text})

    # Отправляем подтверждение пользователю
    await message.reply(f"Ваше анонимное сообщение сохранено. Идентификатор сообщения: {message_id}")


# Обработчик команды /get_message
@dp.message_handler(commands=['get_message'])
async def get_message_command(message: types.Message):
    # Проверяем наличие аргумента (идентификатора сообщения)
    if len(message.text.split()) == 2:
        try:
            # Получаем идентификатор сообщения из аргумента команды
            message_id = int(message.text.split()[1])

            # Ищем сообщение в списке анонимных сообщений по идентификатору
            for msg in messages:
                if msg["message_id"] == message_id:
                    # Отправляем анонимное сообщение
                    await message.reply(f"Анонимное сообщение:nn{msg['text']}")
                    return
            # Если сообщение не найдено
            await message.reply("Сообщение с указанным идентификатором не найдено.")
        except ValueError:
            await message.reply("Некорректный идентификатор сообщения.")
    else:
        await message.reply("Пожалуйста, укажите идентификатор сообщения после команды /get_message.")


# Запускаем бота
if __name__ == '__main__':
    dp.run_polling()