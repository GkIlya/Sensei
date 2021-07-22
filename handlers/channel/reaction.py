from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query_handler(text="cool")
async def cool(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.answer('Тебе понравился этот пост')


@dp.callback_query_handler(text="nocool")
async def cool(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.answer('Тебе не понравился этот пост')
