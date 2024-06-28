from aiogram import Router, types


echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message)
    await message.answer("Я не понимаю вас, поробуйте следующие команды:\n"
    "/start - начать опрос")
async def reverse_words(message: types.Message):
    text = message.text
    words = text.split()
    reversed_words = ' '.join(words[::-1])
    await message.answer(reversed_words)