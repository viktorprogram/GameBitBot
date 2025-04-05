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