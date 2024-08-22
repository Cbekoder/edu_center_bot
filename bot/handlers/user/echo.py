from aiogram.types import Message, ContentType
from aiogram import F
from loader import dp

@dp.message(F.text)
# @dp.message(lambda message: message.text)
async def echo_handler(message: Message) -> None:
    await message.answer("Siz matn yubordingiz")

@dp.message(F.photo)
async def photo_handler(message: Message) -> None:
    # await message.photo
    file_id = message.photo[-1].file_id
    await message.answer(f"Siz photo yubordingiz\nfile id = {file_id}")

@dp.message(F.video)
async def video_handler(message: Message) -> None:
    file_id = message.video.file_id
    await message.answer(f"Siz video yubordingiz\nfile id = {file_id}")

@dp.message(F.document)
async def doc_handler(message: Message) -> None:
    file_id = message.document.file_id
    await message.answer(f"Siz document yubordingiz\nfile id = {file_id}")

@dp.message(F.contact)
async def contact_handler(message: Message) -> None:
    file_id = message.contact.phone_number
    await message.answer(f"Siz contact yubordingiz\nphone id = {file_id}")

@dp.message(F.location)
async def location_handler(message: Message) -> None:
    long = message.location.longitude
    lat = message.location.latitude
    await message.answer(f"Siz contact yubordingiz\nlocation id = {long},{lat}")


