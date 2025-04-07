from telebot.handler_backends import State, StatesGroup

class UserStateInfo(StatesGroup):
    """Класс состояния пользователя"""
    start = State()
    visit_time = State()
    name_state = State()
    choosing_place = State()
