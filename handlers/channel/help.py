from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def helper(message: types.Message):
    await message.answer("C помощью этого бота ты сможешь предлагать"
                         " на публикация посты и мемы")
