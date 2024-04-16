from aiogram import Router, F, types
from aiogram.filters import Command
from config import database


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
    data = await database.fetch(
        """
        SELECT books.* FROM books 
        JOIN genres ON books.genre_id = genres.id
        WHERE genres.name = ?
        """, 
        (genre,),
        fetch_type='all'
    )
    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=kb)
    await message.answer(f'Все наши книги жанра {genre}:')
    for book in data:
        price = book['price']
        name = book['name']
        photo = types.FSInputFile(book['picture'])
        await message.answer_photo(
            photo=photo,
            caption=f'Название книги: {name}\nЦена: {price} сом'
        )