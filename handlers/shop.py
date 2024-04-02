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


@shop_router.message(F.text.lower() == 'хоррор')
async def show_horror(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    print(message.text)
    await message.answer('Все наши книги жанра хоррор', reply_markup=kb)