from GamebitBot.loader import bot
from telebot.types import Message

from keyboards.inline_button import menu_button


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    bot.send_message(chat_id=message.chat.id, text="Добро пожаловать в <b>GameBitBot</b>", parse_mode='html', reply_markup=menu_button())

@bot.message_handler(func=lambda message:True)
def info_gamebit(message: Message):
    text = message.text
    if text == '⌨️🖥Характеристики':
        bot.send_message(chat_id=message.chat.id, text='Тут выводятся характеристики клуба ', )
    elif text == '🌇Интерьер':
        bot.send_message(chat_id=message.chat.id, text='Тут фотто интерьера', )
    elif text == '📫Локация':
        bot.send_message(chat_id=message.chat.id, text='Тут локация',)
    elif text == '💰Прайс':
        bot.send_message(chat_id=message.chat.id, text='Тут прайс',)