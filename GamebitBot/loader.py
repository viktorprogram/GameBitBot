from telebot import TeleBot
from data import config
from telebot import StateMemoryStorage

storage = StateMemoryStorage()
bot = TeleBot(token=config.TOKEN, state_storage=storage)