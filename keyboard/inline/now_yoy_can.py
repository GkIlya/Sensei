from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

can = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Предложить пост📮",
                callback_data="offerpost"
            )
        ],
        [
            InlineKeyboardButton(
                text="Предложить мем🦕",
                callback_data="offermem"
            )
        ],
    ]
)
