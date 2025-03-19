from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states.form_states import Form

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