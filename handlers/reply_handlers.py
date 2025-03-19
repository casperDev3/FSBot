from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_test
from aiogram.fsm.context import FSMContext

from states.form_states import Form

router = Router()


@router.message(lambda message: message.text == "Test")
async def test_handler(message: types.Message):
    await message.answer("""It's test message!""", reply_markup=get_inline_test())

@router.message(lambda message: message.text == "Personal data")
async def test_handler(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("What is your name?", reply_markup=types.ReplyKeyboardRemove())
