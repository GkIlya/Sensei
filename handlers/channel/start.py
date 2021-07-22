from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import CallbackQuery

from config import channels
from keyboard.inline.chek_subscribe import inline_check_sub
from keyboard.inline.now_yoy_can import can
from loader import dp, bot
from states.state_for_channel import Channel


async def check(user_id, channel):
    members = await bot.get_chat_member(chat_id=channel, user_id=user_id)
    return members.is_chat_member()


@dp.message_handler(CommandStart())
async def start_without_subscribe(message: types.Message):
    await message.answer("Бот запущен")
    source_main_message = str()

    for channel in channels:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        source_main_message += f"<a href='{invite_link}'>{chat.title}</a>\n\n"

    main_message = f"""Для полного функционирования бота
вы должны подписаься на следующие каналы:
    
    {source_main_message}"""

    await message.answer(main_message, reply_markup=inline_check_sub)
    await Channel.s1.set()


@dp.callback_query_handler(text="check", state=Channel.s1)
async def check_subscribe(call: CallbackQuery, state: FSMContext):
    main_message = str()
    await call.answer(cache_time=5)
    for channel in channels:
        status = await check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            await call.message.answer("Подписка на каналы оформлена🥇✅\n"
                                      "Tеперь ты можешь:",
                                      reply_markup=can)
            await state.finish()
            await call.message.edit_reply_markup()
        else:
            link = await channel.export_invite_link()
            main_message += f"Тебе нужно подписаться на канал <a href='{link}'>{channel.title}</a>"
    try:
        await call.message.answer(main_message)
    except:
        pass
