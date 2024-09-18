from aiogram.types import InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Функция отправки приветственного сообщения пользователю
async def send_welcome_message(user_id, username):
    # Загрузка фото для приветственного сообщения
    photo = FSInputFile('./data/img.png')
    # Создание текста сообщения с упоминанием пользователя
    caption = f'<a href="tg://user?id={user_id}">Привет</a>! Ты попал в наш чат, располагайся)'

    # Создание кнопки с ссылкой
    button = InlineKeyboardButton(text='Перейти ->', url='https://www.google.com/')

    # Создание и настройка клавиатуры
    builder = InlineKeyboardBuilder()
    builder.add(button)
    markup = builder.as_markup()

    # Возвращение данных для отправки сообщения
    return {
        'photo': photo,
        'caption': caption,
        'markup': markup,
    }
