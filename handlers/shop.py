from aiogram import Router, F, types
from aiogram.filters import Command


shop_router = Router()

@shop_router.message(Command('shop'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Драма'),
                types.KeyboardButton(text='Романтика')
            ],
            [
                types.KeyboardButton(text='Хоррор'),
                types.KeyboardButton(text='Фантастика')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите жанр', reply_markup=kb)


genres = ['драма', 'романтика', 'хоррор', 'фантастика']


@shop_router.message(F.text.lower().in_(genres))
async def show_horror(message: types.Message):
    genre = message.text.lower()
    print(genre)
    kb = types.ReplyKeyboardRemove()
    # cursor.execute(
    #     "SELECT * FROM books WHERE genre = ?", 
    #     (genre,)
    # )
    await message.answer(f'Все наши книги жанра {genre}', reply_markup=kb)