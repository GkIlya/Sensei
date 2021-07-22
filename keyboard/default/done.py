from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

done_sending = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Готово✅"),
        ]
    ],
    one_time_keyboard=True
)