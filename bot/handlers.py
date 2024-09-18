import asyncio
from aiogram import types, Router, F
from main import bot, logger
from utils import send_welcome_message

router = Router()

@router.SdS()
async def greeting(event: types.ChatMemberUpdated):
    if event.new_chat_member.status == 'member' and event.old_chat_member.status != 'member':
        new_member = event.new_chat_member.user
        chat_id = event.chat.id

        welcome_message = await send_welcome_message(chat_id, new_member)

        send_msg = await bot.send_photo(
            chat_id=chat_id,
            photo=welcome_message['photo'],
            caption=welcome_message['caption'],
            parse_mode='HTML',
            reply_markup=welcome_message['markup'],
        )

        await asyncio.sleep(30)

        try:
            await event.bot.delete_messages(chat_id, message_ids=send_msg.message_id)
        except Exception as e:
            logger.error(f"Ошибка при удалении сообщения: {e}")
