from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Test")],
            [KeyboardButton(text="Personal data"), KeyboardButton(text="Send Pic")],
        ],
        resize_keyboard=True
    )
    return keyboard
