@dp.message_handler(commands=['send'])
async def send_message(message: types.Message):
    if message.from_user.id == YOUR_SENDER_ID:  # Замените YOUR_SENDER_ID на нужный идентификатор отправителя
        await bot.send_message(chat_id=YOUR_RECIPIENT_ID, text='Привет, это секретное сообщение!')  # Замените YOUR_RECIPIENT_ID на нужный идентификатор получателя

