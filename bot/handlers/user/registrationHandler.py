from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.states.registrationStates import RegistrationStates
from bot.data.config import ADMINS

from loader import dp, bot

@dp.callback_query(lambda query: query.data.startswith('registration'))
async def registration_handler(query: CallbackQuery, state: FSMContext):
    course = query.data.split(":")[1]
    await state.set_state(RegistrationStates.ism)
    await state.update_data(kurs=course)
    await query.answer(cache_time=10)
    await query.message.answer("Ro'yxatdan o'tish uchun ismingizni kiriting:")


@dp.message(RegistrationStates.ism)
async def ism_handler(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await state.set_state(RegistrationStates.familya)
    await message.answer("Familyangizni kiriting:")

@dp.message(RegistrationStates.familya)
async def familya_handler(message: Message, state: FSMContext):
    familya = message.text
    await state.update_data(familya=familya)
    await state.set_state(RegistrationStates.telefon)
    await message.answer("Aloqaga chiqish uchun "
                         "telefon raqamgizni kiriting:")

@dp.message(RegistrationStates.telefon)
async def telefon_handler(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    data = await state.get_data()
    await state.clear()
    response = (f"Yangi ro'yxatdan o'tgan o'quvchi."
                f"\nIsm: {data['ism']}"
                f"\nFamilya: {data['familya']}"
                f"\nTelefon: {telefon}"
                f"\nKurs: {data['kurs']}")
    await bot.send_message(ADMINS[0], response)
    await message.answer("Muvaffaqqiyatli ro'yxatdan o'tdingiz!")

