import os
from GamebitBot.loader import bot
from telebot.types import Message, InputMediaPhoto

from keyboards.inline_button import menu_button, button_location


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    """Обработка команды старт с выводом блока кнопок с общей информацией"""
    bot.send_message(chat_id=message.chat.id,
                     text=f"<b>{message.from_user.full_name}</b> Добро пожаловать в <b>GameBitBot</b>",
                     parse_mode='html',
                     reply_markup=menu_button())

specifications_text = ('🖥 32" Монитор Samsung Odyssey G5 165Гц, изогнутый \n'
          '⌨️ Механическая клавиатура Defender Black Raven GK-417, 3 цвета, радужная подсветка, 63 кнопки \n'
          '🖱 Игровая мышь компьютерная Redragon Griffin 7 кнопок 7200 DPI \n'
          '🀆 Intel Процессор Core i5-10600KF \n'
          '🕹 Оперативная память HyperX FURY 16 ГБ \n'
          '💾 Kingston Внутренний SSD-диск KC3000 M.2 PCI-E 4.0 \n'
          '📸 ZOTAC Видеокарта GeForce RTX 4060 8 ГБ')


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

@bot.message_handler(func=lambda message:True)
def info_gamebit(message: Message):
    """Вывод информации о клубе"""
    text = message.text
    if text == '⌨️🖥Характеристики':
        bot.send_message(chat_id=message.chat.id, text=specifications_text)

    elif text == '🌇Интерьер':
        open_photo_path, photo = open_photo_to_message(name='interior')
        bot.send_media_group(chat_id=message.chat.id, media=photo)
        close_photo(open_photo_path)

    elif text == '📫Локация':
        photo_location = open((f'{os.getcwd()}\\photo\\location\\location.jpg'), 'rb')
        bot.send_photo(chat_id=message.chat.id,
                       reply_markup=button_location(),
                       photo=photo_location,
                       caption='Мы находимся по адресу <b>Cело Винсады, Подгорная улица, 156Г 2 этаж</b> ',
                       parse_mode='html')
        photo_location.close()

    elif text == '💰Прайс':
        open_photo_path, photo = open_photo_to_message(name='price')
        bot.send_media_group(chat_id=message.chat.id, media=photo)
        close_photo(open_photo_path)

    elif text == '🚨Правила клуба':
        open_photo_path, photo = open_photo_to_message(name='rule')
        bot.send_media_group(chat_id=message.chat.id, media=photo)
        close_photo(open_photo_path)

