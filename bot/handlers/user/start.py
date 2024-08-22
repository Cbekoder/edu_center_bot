from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import html
from bot.keyboards.default.menuKeyboard import menuButtons

from loader import dp

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Assalomu alaykum, {html.bold(message.from_user.full_name)}!"
                         f"\nO'quv markazimizga xush kelibsiz!"
                         f"\nSizga qanday yordam bera olaman?"
                         f"\nKerakli bo'limni tanlang!", reply_markup=menuButtons)
