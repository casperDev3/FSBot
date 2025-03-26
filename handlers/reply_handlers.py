from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_test, get_inline_mod_tasks
from aiogram.fsm.context import FSMContext
from pathlib import Path
from states.form_states import Form
from states.tasks_states import Tasks
import json

router = Router()
BASE_DIR = Path(__file__).resolve().parent.parent


@router.message(lambda message: message.text == "Test")
async def test_handler(message: types.Message):
    await message.answer("""It's test message!""", reply_markup=get_inline_test())


@router.message(lambda message: message.text == "Personal data")
async def pdata_handler(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("What is your name?", reply_markup=types.ReplyKeyboardRemove())


@router.message(lambda message: message.text == "Add Task")
async def task_handler(message: types.Message, state: FSMContext):
    await state.set_state(Tasks.title)
    await message.answer("Enter task title:")

@router.message(lambda message: message.text == "Show Tasks")
async def show_task_handler(message: types.Message):
    await message.answer("Here is your tasks:")
    with open("data/tasks.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        await message.answer(f"{task['title']}", reply_markup=get_inline_mod_tasks(task['id']))

