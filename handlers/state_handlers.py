from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states.form_states import Form
from states.tasks_states import Tasks
from utils.tasks import add_new_task


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
