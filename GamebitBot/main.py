from loader import bot
from handlers.users.start import *
from telebot.custom_filters import StateFilter
from utils.set_my_commands import set_default_commands

if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()

