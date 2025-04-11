from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Personal data"), KeyboardButton(text="My Profile")],
            [KeyboardButton(text="Add Task"),
             KeyboardButton(text="Show Tasks"),
             KeyboardButton(text="Search by name")],
            [KeyboardButton(text="Upload Media"), KeyboardButton(text="Send Pic")],
        ],
        resize_keyboard=True
    )
    return keyboard
