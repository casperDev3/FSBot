from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_test
from aiogram.fsm.context import FSMContext
from pathlib import Path
from states.form_states import Form

router = Router()
BASE_DIR = Path(__file__).resolve().parent.parent

@router.message(lambda message: message.text == "Test")
async def test_handler(message: types.Message):
    await message.answer("""It's test message!""", reply_markup=get_inline_test())

@router.message(lambda message: message.text == "Personal data")
async def test_handler(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("What is your name?", reply_markup=types.ReplyKeyboardRemove())

@router.message(lambda message: message.text == "Send Pic")
async def test_handler(message: types.Message):
    path = BASE_DIR / "assets/media/solo_leveling.jpg"
    await message.answer_photo(
        photo = types.FSInputFile(path),
        caption = "It's a caption!"
    )
