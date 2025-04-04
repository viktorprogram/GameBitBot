from GamebitBot.loader import bot
from telebot.types import Message
from GamebitBot.states.state_user import UserStateInfo

from keyboards.inline_button import menu_button


@bot.message_handler(commands=['menu'])
def command_start(message: Message):
    """Вывод меню информации"""
    # bot.set_state(user_id=message.from_user.id, chat_id=message.chat.id, state=UserStateInfo.start)
    bot.send_message(chat_id=message.chat.id, text='Клуб GAmeBit', reply_markup=menu_button())

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






