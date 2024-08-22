from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kurslarButtons = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Kompyuter savodxonligi💻'),
            KeyboardButton(text='Grafik dizayn🎨')
        ],
        [
            KeyboardButton(text='Frontend💈'),
            KeyboardButton(text='Backend⚙️'),
            KeyboardButton(text='Android📲')
        ],
        [
            KeyboardButton(text='Asosiy menu🔙')
        ]
    ]
)