import datetime
from typing import List

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# def menu_button() -> InlineKeyboardMarkup:
#     """Кнопки с общей информацией"""
#     markup = InlineKeyboardMarkup()
#     but_1 = InlineKeyboardButton('Характеристики', callback_data='specifications')
#     but_2 = InlineKeyboardButton('Локация', callback_data='location')
#     but_3 = InlineKeyboardButton('Интерьер', callback_data='interior')
#     but_4 = InlineKeyboardButton('Прайс', callback_data='price')
#     markup.add(but_1,but_2,but_3,but_4)
#     return markup

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
    but_1 = InlineKeyboardButton(text='Машрту', url='https://yandex.ru/maps/-/CHVVBOOh')
    markup.add(but_1)
    return markup

def time_list() -> List[str]:
    """Функция создает список со временем на сутки, от текущей даты"""
    time_now = str(datetime.datetime.now().time().strftime(format='%H:%M'))
    list_time = []



    if int(time_now[3:]) >= 30:
        if int(time_now[:2]) == 23:
            now_time = '00:30'
            list_time.append(now_time)
        else:
            now_time = str(int(time_now[0:2]) + 1) + ':30'
            list_time.append(now_time)
    else:
        if int(time_now[:2]) == 23:
            now_time = '00:00'
            list_time.append(now_time)
        else:
            now_time = str(int(time_now[:2]) + 1) + ':00'
            list_time.append(now_time)

    date_format = datetime.datetime.strptime(now_time, '%H:%M')
    for h in range(49):
        date_format += datetime.timedelta(minutes=30)
        list_time.append(date_format.time().strftime(format='%H:%M'))

    return list_time



def visit_time_button() -> InlineKeyboardMarkup:
    """Спсок кнопок для выбора время бронирования"""
    markup = InlineKeyboardMarkup()
    new_list = [InlineKeyboardButton(text=time,callback_data=f'{time}_visit_time') for time in time_list()]
    markup.add(*new_list, row_width=4)

    return markup

def end_time_button() -> InlineKeyboardMarkup:
    """Спсок кнопок для выбора время бронирования"""
    markup = InlineKeyboardMarkup()
    new_list = [InlineKeyboardButton(text=time,callback_data=f'{time}_end_time') for time in time_list()]
    markup.add(*new_list, row_width=4)

    return markup

def request_contact_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    but_1 = KeyboardButton(text="Отправить номер телефона", request_contact=True)
    markup.add(but_1)
    return markup

