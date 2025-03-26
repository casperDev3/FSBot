from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_test() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="test1", callback_data="test_btn_1"),
         InlineKeyboardButton(text="test2", callback_data="test_btn_2")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_inline_test_2() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="test3", callback_data="test_btn_3"),
         InlineKeyboardButton(text="test4", callback_data="test_btn_4")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_inline_mod_tasks(id_task) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Виконано", callback_data="mod_task_done_" + str(id_task))],
        [InlineKeyboardButton(text="Видалити", callback_data="mod_task_del_" + str(id_task))],
        [InlineKeyboardButton(text="Редагувати", callback_data="mod_task_edit_" + str(id_task))],
        [InlineKeyboardButton(text="Повернутися", callback_data="mod_task_back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
