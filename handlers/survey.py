from aiogram import Router, F, types
from config import database


survey_router = Router()


class BookSurvey(StatesGroup):
    name = State()
    age = State()
    occupation = State()
    salary_or_grade = State()


# Обработчик команды /start
@dp.message_handler(Command("start"))
async def start_survey(message: types.Message, state: FSMContext):
    await BookSurvey.name.set()
    await message.answer("Добро пожаловать в наш опрос! Как вас зовут?")

# Обработчик имени
@dp.message_handler(state=BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(f"Спасибо, {name}!")
    await state.update_data(name=name)
    await BookSurvey.age.set()
    await message.answer("Сколько вам лет?")

# Обработчик возраста
@dp.message_handler(state=BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, введите число.")
        return
    age = int(age)
    if age < 7 or age > 60:
        await message.answer("Пожалуйста, введите возраст от 7 до 60 лет.")
        return

    await state.update_data(age=age)
    if age > 18:
        await BookSurvey.occupation.set()
        await message.answer("Какая у вас профессия?")
    else:
        await BookSurvey.salary_or_grade.set()
        await message.answer("Как ваши успехи в школе? Введите средний балл.")

# Обработчик профессии
@dp.message_handler(state=BookSurvey.occupation)
async def process_occupation(message: types.Message, state: FSMContext):
    occupation = message.text
    await state.update_data(occupation=occupation)
    await BookSurvey.salary_or_grade.set()
    await message.answer("Введите вашу заработную плату.")

# Обработчик заработной платы или оценки
@dp.message_handler(state=BookSurvey.salary_or_grade)
async def process_salary_or_grade(message: types.Message, state: FSMContext):
    salary_or_grade = message.text
    async with state.proxy() as data:
        age = data['age']
    
    if age > 18:
        await message.answer(f"Вы выбрали заработную плату: {salary_or_grade}")
    else:
        await message.answer(f"Вы выбрали оценку: {salary_or_grade}")
    
    await state.update_data(salary_or_grade=salary_or_grade)
    await message.answer("Спасибо, что ответили на все вопросы!")

    # Сохранение данных в базу данных
    async with state.proxy() as data:
        name = data['name']
        age = data['age']
        occupation = data['occupation']
        salary_or_grade = data['salary_or_grade']
        
        # Вставка данных в базу данных
        await database.execute(
            "INSERT INTO surveys (name, age, occupation, salary, grade) VALUES (?, ?, ?, ?, ?)",
            (name, age, occupation, salary_or_grade, None if age > 18 else salary_or_grade)
        )

    await state.finish()

# Обработчик команды /stop
@dp.message_handler(Command("stop"))
@dp.message_handler(types.ContentType.TEXT, state="*", commands=["stop"])
async def stop(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Опрос завершен. Спасибо за участие!")

   
    data = await state.get_data()
    print(data)
    await state.clear()

# Запуск бота
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

@survey_router.message(Command("stop"))
@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")
