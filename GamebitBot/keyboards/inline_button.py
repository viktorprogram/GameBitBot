from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from utils.utils_bot import time_list

def menu_button() -> ReplyKeyboardMarkup:
    """Кнопки с общей информацией"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    but_0 = KeyboardButton('Забронировать', )
    but_1 = KeyboardButton('⌨️🖥Характеристики', )
    but_2 = KeyboardButton('📫Локация', )
    but_3 = KeyboardButton('🌇Интерьер', )
    but_4 = KeyboardButton('💰Прайс', )
    but_5 = KeyboardButton('🚨Правила клуба', )
    markup.add(but_0)
    markup.add(but_1,but_2,but_3,but_4, row_width=2)
    markup.add(but_5)
    return markup

def button_location() -> InlineKeyboardMarkup:
    """Кнопка с ссылкой на карте с адресом"""
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton(text='Маршрут', url='https://yandex.ru/maps/-/CHVVBOOh')
    markup.add(but_1)
    return markup


def visit_time_button(name_time) -> InlineKeyboardMarkup:
    """Спсок кнопок для выбора времени бронирования"""
    markup = InlineKeyboardMarkup()
    new_list = [InlineKeyboardButton(text=time,callback_data=f'{time}_{name_time}') for time in time_list()]
    markup.add(*new_list, row_width=4)
    return markup

def choosing_place_button() -> InlineKeyboardMarkup:
    """Спсок кнопок для выбора компьютера"""
    markup = InlineKeyboardMarkup()
    but_0 = InlineKeyboardButton(text='Стандарт №1', callback_data='pk_st_1')
    but_1 = InlineKeyboardButton(text='Стандарт №2', callback_data='pk_st_2')
    but_2 = InlineKeyboardButton(text='Стандарт №3', callback_data='pk_st_3')
    but_3 = InlineKeyboardButton(text='Стандарт №4', callback_data='pk_st_4')
    but_4 = InlineKeyboardButton(text='Стандарт №5', callback_data='pk_st_5')
    but_5 = InlineKeyboardButton(text='VIP №1', callback_data='pk_vip_1')
    but_6 = InlineKeyboardButton(text='VIP №2', callback_data='pk_vip_2')
    but_7 = InlineKeyboardButton(text='PS 5', callback_data='pk_ps')
    markup.add(but_0, but_1, but_2, but_3, but_4, row_width=3)
    markup.add( but_5, but_6, but_7, row_width=2)
    return markup

def request_contact_button():
    """Кнопка с отправкой номера телефона"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    but_1 = KeyboardButton(text="Отправить номер телефона", request_contact=True)
    markup.add(but_1)
    return markup

