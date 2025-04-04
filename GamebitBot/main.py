from loader import bot
from handlers.users.start import *
from telebot.custom_filters import StateFilter
from utils.set_my_commands import set_default_commands

# on_startup()
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()

