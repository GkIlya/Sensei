import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import Groups, Admin
from loader import dp


@dp.message_handler(Groups(), Command("set_photo"), Admin())
async def set_chat_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = photo.download(destination=io.BytesIO)
    input_file = types.InputFile(path_or_bytesio=photo)
    await message.chat.set_photo(photo=input_file)
    await message.answer("Фото группы изменено✅")


@dp.message_handler(Groups(), Command("set_description"), Admin())
async def set_chat_description(message: types.Message):
    source_message = message.reply_to_message
    text = source_message.text
    await message.chat.set_description(description=text)
    await message.answer("Описание группы изменено✅")


@dp.message_handler(Groups(), Command("set_title"), Admin())
async def set_chat_title(message: types.Message):
    source_message = message.reply_to_message
    text = source_message.text
    await message.chat.set_title(title=text)
    await message.answer("Название группы изменено✅")


@dp.message_handler(Groups(), Command("pin"), Admin())
async def pin_message(message: types.Message):
    message_to_pin = message.reply_to_message.message_id
    await message.chat.pin_message(message_id=message_to_pin)
    await message.answer("Сообщение зкреплено✅")


@dp.message_handler(Command("unpin"), Admin())
async def unpin_all_message(message: types.Message):
    await message.chat.unpin_all_messages()
    await message.answer("Сообщения откреплены✅")

