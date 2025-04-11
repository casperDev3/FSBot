from aiogram import types, Router
from aiogram.types import FSInputFile

from keyboards.inline_keyboards import get_inline_test, get_inline_mod_tasks
from aiogram.fsm.context import FSMContext
from pathlib import Path
from states.form_states import Form
from states.tasks_states import Tasks
from states.search_states import SearchEmployeeByName
from states.upload_media_states import UploadMediaStates
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

@router.message(lambda message: message.text == "Search by name")
async def task_handler(message: types.Message, state: FSMContext):
    await state.set_state(SearchEmployeeByName.query)
    await message.answer("Enter employee name:")

@router.message(lambda message: message.text == "Upload Media")
async def media_handler(message: types.Message, state: FSMContext):
    await state.set_state(UploadMediaStates.wait_for_photo)
    await message.answer("Please sent photo:")


@router.message(lambda message: message.text == "My Profile")
async def profile_handler(message: types.Message):
    # Check if the user is in the database
    with open("data/employee.json", "r") as f:
        users = json.load(f)

    # get the user data
    data_user = [user for user in users if user['id'] == message.from_user.id][0]

    # format the profile information
    txt = "🌟 Ваш профіль користувача 🌟\n\n"
    txt += f"👤 Повне ім'я: {data_user['full_name']}\n"
    txt += f"🔹 Юзернейм: {data_user['username']}\n"
    txt += f"🤖 Чи є бот: {'Так' if data_user['is_bot'] else 'Ні'}\n"
    txt += f"🗣 Мова: {data_user['language_code']}\n"
    txt += f"🆕 Статус: {data_user['status']}\n"
    txt += f"🏢 Роль: {data_user['role']}\n\n"
    txt += f"📝 Опис:\n{data_user['description']}\n\n"

    # Send the profile information as a photo
    photo_file = FSInputFile(data_user['profile_img'])
    await message.answer_photo(photo=photo_file, caption=txt)

