from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.utils.token import TokenValidationError
import asyncio

from config import TELEGRAM_BOT_TOKEN

API_TOKEN = TELEGRAM_BOT_TOKEN

# Инициализация бота и диспетчера
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Устанавливаем parse_mode
)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Используй /help, чтобы узнать больше.")

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Доступные команды:\n/start - Начать работу\n/help - Помощь")

# Обработчик всех сообщений
@dp.message()
async def echo(message: Message):
    await message.answer(f"Введите /start, чтобы Начать работу")

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)  # Пропуск накопленных апдейтов

if __name__ == '__main__':
    asyncio.run(main())