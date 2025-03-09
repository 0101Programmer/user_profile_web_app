import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message

from config import TELEGRAM_BOT_TOKEN, FASTAPI_BASE_URL

API_TOKEN = TELEGRAM_BOT_TOKEN

# Инициализация бота и диспетчера
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Устанавливаем parse_mode
)
dp = Dispatcher()

# Обработчик всех входящих сообщений
@dp.message()
async def to_web_app(message: Message):
    username = message.from_user.username  # Получаем username

    # Проверяем, есть ли username
    if not username:
        await message.answer("У вас нет username. Пожалуйста, установите его в настройках Telegram.")
        return

    # Создаем клавиатуру с динамической ссылкой
    to_web_app_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть приложение",
                    url=f"{FASTAPI_BASE_URL}/page_for/{username}"  # Подставляем username в ссылку
                )
            ]
        ]
    )
    await message.answer(f"Добро пожаловать! Чтобы перейти в приложение нажми на кнопку",
                         reply_markup=to_web_app_kb)

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)  # Пропуск накопленных апдейтов

if __name__ == '__main__':
    asyncio.run(main())