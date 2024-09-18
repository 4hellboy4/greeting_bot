import logging
import os
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from bot.handlers import router

# Загрузка переменных окружения из файла .env
load_dotenv()

dp = Dispatcher()
# Подключение роутера
dp.include_router(router)

bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
