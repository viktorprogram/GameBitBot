# from GamebitBot.loader import bot
from telebot.types import Message, BotCommand
from GamebitBot.data.config import DEFAULT_COMMANDS


def set_my_commands(bot):
    """Установка команд из списка в конфигурации"""
    bot.set_my_commands([BotCommand(*i) for i in DEFAULT_COMMANDS])
