from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_check_sub = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Проверить подписки☑️",
                                 callback_data="check")
        ]
    ]
)
