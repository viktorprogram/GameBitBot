import os
from loader import bot
from telebot.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.inline_button import menu_button, button_location, visit_time_button, \
    request_contact_button, choosing_place_button
from states.state_user import UserStateInfo
from utils.utils_bot import info_pk_user, open_photo_to_message, close_photo


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    """Обработка команды старт с выводом блока кнопок с общей информацией"""
    bot.set_state(message.from_user.id, UserStateInfo.start, message.chat.id)
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

@bot.message_handler(state=UserStateInfo.start)
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
                       caption='Мы находимся по адресу <b>с. Винсады, Подгорная улица, 156Г 2 этаж</b> ',
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
    elif text == 'Забронировать':
          bot.send_message(chat_id=message.chat.id, reply_markup=visit_time_button(name_time='visit_time'), text='Выберите время посещения клуба')


@bot.callback_query_handler(func=lambda call: call.data.endswith('visit_time'))
def visit_time_user(call: CallbackQuery):
    """Обработка нажатия кнопки о времени посещения, и занося ее в информацию пользователя"""
    bot.set_state(user_id=call.from_user.id, chat_id=call.message.chat.id, state=UserStateInfo.visit_time)
    with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data:
        data['visit_time'] = call.data[:5]
    bot.edit_message_text(text=f'Вы выбрали время посещения {call.data[:5]} выберите до какого времени ',
                          chat_id=call.message.chat.id,
                          message_id=call.message.message_id, reply_markup=visit_time_button(name_time='end_time')
                          )

@bot.callback_query_handler(func=lambda call: call.data.endswith('end_time'))
def end_time_user(call: CallbackQuery):
    """Обработка нажатия кнопки о времени прекращения посещения, и занося ее в информацию пользователя"""
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['end_time'] = call.data[:5]
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text='Выберите пожалуйста компьютер',
                          reply_markup=choosing_place_button())

@bot.callback_query_handler(func=lambda call: call.data.startswith('pk'))
def choosing_place_user(call: CallbackQuery):
    """Получение выброннаго места для бронирования"""
    bot.set_state(user_id=call.from_user.id, chat_id=call.message.chat.id, state=UserStateInfo.name_state)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['choosing_place'] = call.data[3:]
    bot.edit_message_text(text='Напишите свое имя', chat_id=call.message.chat.id, message_id=call.message.message_id)
    # bot.register_next_step_handler(call.message, name_user)

@bot.message_handler(state=UserStateInfo.name_state)
def name_user(message: Message):
    sent_message = bot.send_message(chat_id=message.chat.id,
                                    text='Для завершения бронирования, отправьте нам пожалуйста номер телефона, для связи с вами, '
                                         'для этого нажмите кнопку снизу 👇'
                                         '(ваш номер телефона нигде не сохранятеся, он нужен только для связи с вами!)',
                                    reply_markup=request_contact_button())
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name_user'] = message.text
        data['sent_message_phone'] = sent_message

@bot.message_handler(content_types=['contact'])
def phone(message: Message):
    """Получение номера телефона и отправка сообщения о бронировании администратору"""
    try:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            visit_time = data.get('visit_time')
            end_time = data.get('end_time')
            name = data.get('name_user')
            full_choosing_place = info_pk_user(data.get('choosing_place'))
            sent_message = data.get('sent_message_phone')
        bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
    except AttributeError:
        pass
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id='259061505', text=f'Пользователь - {name} \n'
                                               f'Забронировал на время с {visit_time} до {end_time} \n'
                                               f'Компьютер - {full_choosing_place} \n'
                                               f'номер телефона - {message.contact.phone_number}')
    bot.send_message(chat_id=message.chat.id, text=f'{name}, спасибо что забронировали  \n'
                                                        f'Компьютер - {full_choosing_place} \n'
                                                        f'на время с {visit_time} до {end_time} \n'
                                                        f'<b>Если вы не успели ко времени бронирования, бронь продержится 15 минут, '
                                                        f'после чего компьютер будет свободен</b>', parse_mode='html',
                          reply_markup=ReplyKeyboardRemove())



