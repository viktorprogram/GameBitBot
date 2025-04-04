from telebot.custom_filters import StateFilter
from loader import bot
from utils.set_my_commands import set_my_commands


# storage = StateMemoryStorage()
# bot = TeleBot(token=config.TOKEN, state_storage=storage)

#
# def on_startup():
#     utils.notify_admins("Start Bot")
#     utils.set_my_commands()
#     bot.infinity_polling(skip_pending=True)


# on_startup()

if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    set_my_commands(bot)
    bot.infinity_polling()