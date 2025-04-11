from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import InputFile, FSInputFile
import os

from states.form_states import Form
from states.tasks_states import Tasks
from states.search_states import SearchEmployeeByName
from states.upload_media_states import UploadMediaStates
from utils.tasks import add_new_task
from utils.search import search_employee_by_name
from utils.users import edit_employee_field

router = Router()

@router.message(Form.name)
async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer("How old are you?")

@router.message(Form.age)
async def age_handler(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(f"Your name is {data['name']} and you are {data['age']} years old.")
    await state.clear()

@router.message(Tasks.title)
async def tsk_title_handler(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(Tasks.description)
    await message.answer("Please enter task description:")

@router.message(Tasks.description)
async def tsk_desc_handler(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Tasks.link)
    await message.answer("Please enter task link:")

@router.message(Tasks.link)
async def tsk_link_handler(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    data = await state.get_data()
    add_new_task(data)
    await state.clear()

@router.message(SearchEmployeeByName.query)
async def tsk_link_handler(message: types.Message, state: FSMContext):
    await state.update_data(query=message.text)
    data = await state.get_data()
    msg_text = search_employee_by_name(data['query'])
    await message.answer(msg_text)
    await state.clear()


@router.message(UploadMediaStates.wait_for_photo)
async def photo_handler(message: types.Message, state: FSMContext):
    # download photo
    photo = message.photo[-1]
    destination_folder = "media"
    os.makedirs(destination_folder, exist_ok=True)
    file_path = os.path.join(destination_folder, f"{photo.file_unique_id}.jpg")
    file_info = await message.bot.get_file(photo.file_id)
    await message.bot.download_file(file_info.file_path, destination=file_path)

    # write path to employee.json
    saved_photo = edit_employee_field(message.from_user.id, "profile_img", file_path)
    if saved_photo:
        await message.answer("Photo saved successfully!")

    # send photo use file path
    photo_file = FSInputFile(file_path)
    await message.answer_photo(photo=photo_file, caption="Your photo is here:")

    # clear state
    await state.clear()
