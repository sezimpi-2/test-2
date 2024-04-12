from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database


survey_router = Router()


# FSM - Finite State Machine - конечный автомат
class BookSurvey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    genre = State()


@survey_router.message(Command("stop"))
@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")


@survey_router.callback_query(F.data == "survey")
async def start_survey(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookSurvey.name)
    await cb.message.answer("Как вас зовут?")


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer(f"Сколько вам лет, {message.text}?")


@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    if int(age) < 10 or int(age) > 100:
        await message.answer("Пожалуйста, введите возраст от 10 до 100")
        return
    await state.update_data(age=int(age))
    await state.set_state(BookSurvey.gender)
    await message.answer("Укажите ваш пол?")


@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(BookSurvey.genre)
    data = await state.get_data()
    print("!", data)
    await message.answer("Ваш любимый жанр художественной литературы?")


@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    print("~", data)
    # сохр в БД
    # {'name': 'Иван', 'age': 20, 'gender': 'муж', 'genre': 'драма'}
    await database.execute(
        "INSERT INTO survey (name, age, gender, genre) VALUES (?, ?, ?, ?)", 
        (data["name"], data["age"], data["gender"], data["genre"])
    )
    await message.answer("Спасибо за пройденный опрос!")
    await state.clear()