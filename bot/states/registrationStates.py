from aiogram.fsm.state import StatesGroup, State

class RegistrationStates(StatesGroup):
    ism = State()
    familya = State()
    telefon = State()
    kurs = State()