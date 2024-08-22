from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuButtons = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Natijalar")
        ],
        [
            KeyboardButton(text="Tadbirlar"),
            KeyboardButton(text="Aloqa")
        ],

    ]
)
