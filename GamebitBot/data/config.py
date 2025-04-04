from dotenv import find_dotenv, load_dotenv
from environs import Env
import os
# env = Env()
# env.read_env()
if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
# TOKEN = env.str("TOKEN")
TOKEN = os.getenv("TOKEN")
#ADMINS = env.list("ADMINS")

DEFAULT_COMMANDS = (
    ('start', 'Запуск бота'),
)