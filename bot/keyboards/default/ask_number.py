from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

number_request = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Telefon raqami ☎️", request_contact=True)]
    ]
)