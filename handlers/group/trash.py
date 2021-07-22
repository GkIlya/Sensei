from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def delete_of_trash(message: types.Message):
    await message.delete()
