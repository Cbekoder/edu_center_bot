from aiogram.types import Message
from bot.keyboards.default.menuKeyboard import menuButtons
from bot.keyboards.inline.registrationKeyboard import registerButton

from loader import dp

@dp.message(lambda message: message.text == "Kompyuter savodxonligi💻")
async def komputerSavodHandler(message: Message):
    response = """Kompyuter savodxonlik kursi

Davomiyliygi: 1 oy
O'qituvchi: Shukrullo Zaylobiddinov

Nimalar o'qitiladi: MS office dasturlari, Google doc, sheet, slide va boshqalar"""
    await message.answer(response, reply_markup=registerButton("KompyuterSavodxonligi"))


@dp.message(lambda message: message.text == "Asosiy menu🔙")
async def komputerSavodHandler(message: Message):
    await message.answer("Asosiy menu:", reply_markup=menuButtons)