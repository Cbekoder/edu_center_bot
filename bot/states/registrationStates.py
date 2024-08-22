from aiogram.fsm.state import StatesGroup, State

class RegistrationStates(StatesGroup):
    ism = State()
    familya = State()
    photo = State()
    telefon = State()
    kurs = State()
    longitude = State()
    latitude = State()