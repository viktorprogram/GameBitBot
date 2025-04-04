from telebot.handler_backends import State, StatesGroup

class UserStateInfo(StatesGroup):
    """Класс состояния пользователя"""
    start = State()
    specifications = State()
    location = State()
    interior = State()
    price = State()
    not_state = State()