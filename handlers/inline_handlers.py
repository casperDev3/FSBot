from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_test_2
import json

router = Router()


@router.callback_query(lambda c: c.data.startswith("test_btn_"))
async def test_callback_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == "test_btn_1":
        await callback_query.answer('You pressed first Inline Button')
    elif data == "test_btn_2":
        await callback_query.message.delete()
        await callback_query.message.answer('You pressed second Inline Button', reply_markup=get_inline_test_2())


@router.callback_query(lambda c: c.data.startswith("mod_task_"))
async def mod_task_callback_handler(callback_query: types.CallbackQuery):
    data = callback_query.data
    with open("data/tasks.json", "r") as file:
        tasks = json.load(file)

    if data.startswith("mod_task_del_"):
        id_task = int(data.split("_")[-1])
        tasks = [task for task in tasks if task["id"] != id_task]
        with open("data/tasks.json", "w") as file:
            json.dump(tasks, file)
        await callback_query.message.answer("Task deleted. New task List:")
        # for t in tasks:
        #     await callback_query.message.answer(f"{t['id']}. {t['task']}")


