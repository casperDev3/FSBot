from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Test")],
            [KeyboardButton(text="Personal data"), KeyboardButton(text="Send Pic")],
            [KeyboardButton(text="Add Task"), KeyboardButton(text="Show Tasks")],
            [KeyboardButton(text="Search by name")],
        ],
        resize_keyboard=True
    )
    return keyboard
