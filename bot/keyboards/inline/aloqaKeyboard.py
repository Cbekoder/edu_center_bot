from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

aloqaButtons = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text="Telegram", url='https://t.me/cbekoder')],
        [InlineKeyboardButton(text="Youtube", url='https://www.youtube.com/@Codialuz/')]

        # [InlineKeyboardButton(text="Youtube", url='+998914828422')]
    ]
)