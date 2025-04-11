import os
import datetime
from typing import List
from telebot.types import InputMediaPhoto


def info_pk_user(choosing_place: str) -> str:
    """Получение строки с выбором места, и отправка уточняющей справки"""
    try:
        if choosing_place.startswith('st'):
            return f'зал стандарт, ПК № {choosing_place[-1]}'
        elif choosing_place.startswith('vip'):
            return f'зал VIP, ПК № {choosing_place[-1]}'
        else:
            return 'PS-5'
    except AttributeError:
        return 'Ошибочка, попробуйте еще раз'

def open_photo_to_message(name: str):
    """Функция чтения изображения для отправки"""
    open_photo = [open((f'{os.getcwd()}\\photo\\{name}\\{path}'), 'rb') for path in
                          os.listdir(f'{os.getcwd()}\\photo\\{name}')]
    media_photo = [InputMediaPhoto(i) for i in open_photo]
    return open_photo, media_photo

def close_photo(list_open_photo: list):
    """Функция для закрытия фотографий"""
    for interior in list_open_photo: interior.close()
    return

def time_list() -> List[str]:
    """Функция создает список со временем для создания кнопок"""
    time_now_3 = datetime.datetime.now() + datetime.timedelta(hours=3)
    #time_now = str(datetime.datetime.now().time().strftime(format='%H:%M'))
    time_now = time_now_3.time().strftime(format='%H:%M')
    list_time = []

    if 2 < int(time_now[:2]) < 12:
        now_time = '12:00'
        list_time.append(now_time)
    elif int(time_now[3:]) >= 30:
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
    while int(date_format.time().strftime(format='%H:%M')[:2]) != 2:
        date_format += datetime.timedelta(minutes=30)
        list_time.append(date_format.time().strftime(format='%H:%M'))
    return list_time

time_list()
