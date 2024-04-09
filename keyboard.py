from aiogram import types


def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ],
            [   types.InlineKeyboardButton(text="Наш инстаграм", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate_us")
            ],
            [
                types.InlineKeyboardButton(text="Пройти опрос", callback_data="survey")
            ]
        ]
    )
    return kb