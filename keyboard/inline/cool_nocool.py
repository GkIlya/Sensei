from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cool = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="😂",
                                 callback_data="cool"),
            InlineKeyboardButton(text="😑",
                                 callback_data="nocool")
        ]
    ]
)