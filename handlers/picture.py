from aiogram import Router, types
from aiogram.filters import Command


picture_router = Router()

@picture_router.message(Command('picture'))
async def send_picture(message: types.Message):
    file = types.FSInputFile('images/cat.jpg')
    await message.answer_photo(photo=file, caption='Котейка')
