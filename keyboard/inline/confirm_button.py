from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да✅",
                                 callback_data="Yes"),

            InlineKeyboardButton(text="Нет❌",
                                 callback_data="No")
        ]
    ]
)

offer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Одобрить пост👌",
                                 callback_data="approve"),
            InlineKeyboardButton(text="Отклонить пост🚫",
                                 callback_data="disapprove")
        ]
    ]
)
