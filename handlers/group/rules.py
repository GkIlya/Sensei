from asyncio import sleep

from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from filters import Groups, Admin
from loader import dp


@dp.message_handler(Groups(), Text(contains="жаба", ignore_case=True))
async def kick_of_members(message: types.Message):
    await message.reply("Mат запрещен😡")
    await sleep(1)
    await message.chat.kick(user_id=message.from_user.id,
                            revoke_messages=True)


@dp.message_handler(Groups(), Command("bun"), Admin())
async def bun_members(message: types.Message):
    name_of_user = message.reply_to_message.from_user.full_name
    user_id = message.reply_to_message.from_user.id
    await message.chat.promote(
        user_id=user_id,
        can_promote_members=False,
        can_pin_messages=False,
        can_edit_messages=False,
        can_restrict_members=False,
        can_delete_messages=False,
        can_post_messages=False,
        can_invite_users=True,
        can_change_info=False)
    await message.answer(f"Для пользователя {name_of_user}\n"
                         f"Sensei изменил права")


@dp.message_handler(Groups(), Command("unbun"), Admin())
async def bun_members(message: types.Message):
    name_of_user = message.reply_to_message.from_user.full_name
    user_id = message.reply_to_message.from_user.id
    await message.chat.unban(user_id=user_id, only_if_banned=True)

    await message.answer(f"Sensei вернул права\n"
                         f"Ползователю {name_of_user}")