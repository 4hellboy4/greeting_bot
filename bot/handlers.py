import asyncio
from aiogram import types, Router
from aiogram.filters import ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER

from bot.utils import send_welcome_message

router = Router()


# Обработчик события, когда пользователь присоединяется к чату
@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(message: types.ChatMemberUpdated):
    from bot.loader import bot
    try:
        chat_id = message.chat.id
        new_member = message.from_user
        username = new_member.full_name
        id_user = new_member.id

        # Получение приветственного сообщения
        welcome_message = await send_welcome_message(id_user, username)

        # Отправка приветственного фото
        send_msg = await bot.send_photo(
            chat_id=chat_id,
            photo=welcome_message['photo'],
            caption=welcome_message['caption'],
            parse_mode='HTML',
            reply_markup=welcome_message['markup'],
        )

        # Задержка перед удалением сообщения
        await asyncio.sleep(30)

        # Удаление сообщения
        await bot.delete_message(chat_id=chat_id, message_id=send_msg.message_id)
    except Exception as e:
        print(f"Something went wrong: {e}")
