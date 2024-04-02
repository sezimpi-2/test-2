import asyncio
from aiogram import Bot
import logging

from config import bot, dp, set_my_menu
from handlers.start import start_router
from handlers.generic_answer import echo_router
from handlers.picture import picture_router
from handlers.shop import shop_router


async def main():
    await set_my_menu()
    # привязка роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    
    # в самом конце!
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())