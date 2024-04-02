from aiogram import Router, F, types
from aiogram.filters import Command
from keyboard import start_keyboard


start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет!, {message.from_user.first_name}', reply_markup=start_keyboard())


@start_router.callback_query(F.data == "about_us")
async def about_us(cb: types.CallbackQuery):
    print(cb.data)
    # await cb.answer("О нас")
    await cb.answer()
    await cb.message.answer("Наш сайт: https://geeks.kg")