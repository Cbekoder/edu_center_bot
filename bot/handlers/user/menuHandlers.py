from aiogram.types import Message
from bot.keyboards.default.kurslarKeyboard import kurslarButtons
from bot.keyboards.inline.aloqaKeyboard import aloqaButtons
from loader import dp

@dp.message(lambda message: message.text == 'Kurslar')
async def Kurslar_handler(message: Message):
    await message.answer("Bizning o'quv markazda quyidagi kurslar mavjud:",
                         reply_markup=kurslarButtons)

@dp.message(lambda message: message.text == 'Tadbirlar')
async def Tadbirlar_handler(message: Message):
    pass

@dp.message(lambda message: message.text == 'Natijalar')
async def Natijalar_handler(message: Message):
    pass

@dp.message(lambda message: message.text == 'Aloqa')
async def Aloqa_handler(message: Message):
    await message.answer("O'quv markaz adminstratori bilan bo'g'lanish:",
                         reply_markup=aloqaButtons)
    await message.answer_location(longitude=40.44473, latitude=71.41830)