import asyncio
from aiogram import types, Router, F
from bot.utils import send_welcome_message

router = Router()


@router.message(F.new_chat_members)
async def greeting(message: types.Message):
    # from bot.loader import bot
    chat_id = message.chat.id
    for new_member in message.new_chat_members:
        username = new_member.full_name
        id_user = new_member.id

        welcome_message = await send_welcome_message(id_user, username)

        send_msg = await message.bot.send_photo(
            chat_id=chat_id,
            photo=welcome_message['photo'],
            caption=welcome_message['caption'],
            parse_mode='HTML',
            reply_markup=welcome_message['markup'],
        )

        await asyncio.sleep(30)

        await message.bot.delete_message(chat_id=chat_id, message_id=send_msg.message_id)

@router.message(F.left_chat_member)
async def bye_bye(message: types.Message):
    # from bot.loader import bot
    print('left')
    chat_id = message.chat.id
    left_user = message.left_chat_member
    user_id =left_user.id
    username = left_user.full_name

    left_message = f'Пользователь <a href="tg://user?id={user_id}">{username}</a>! покинул чат.'
    send_msg = await message.bot.send_message(chat_id=chat_id, text=left_message, parse_mode='HTML')

    await asyncio.sleep(10)

    await message.bot.delete_message(chat_id=chat_id, message_id=send_msg.message_id)