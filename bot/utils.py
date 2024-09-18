from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def send_welcome_message(user_id, username):
    photo = open('../data/img.png', 'rb')
    caption = f'Привет, <a href="tg://user?id={user_id}">{username}</a>! Ты попал в наш чат, располагайся)'

    button = InlineKeyboardButton(text='Перейти ->', url='https://www.google.com/')
    markup = InlineKeyboardMarkup.add(button)

    return {
        'photo': photo,
        'caption': caption,
        'markup': markup,
    }
