from telebot.types import Message, BotCommand
from GamebitBot.data.config import DEFAULT_COMMANDS


def set_default_commands(bot):
    """Установка команд из списка в config"""
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
