# bot/keyboards/inline/registrationKeyboard.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def registerButton(course: str):
    registrationButton = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ro'yxatdan o'tish",
                                     callback_data=f"registration:{course}"),
            ]
        ]
    )
    return registrationButton