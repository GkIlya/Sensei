from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from config import admins


class Groups(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


class Users(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in types.ChatType.PRIVATE


class Admin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.from_user.id in admins
