import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


START_MESSAGE = (
    "Привет! Это бот, который поможет тебе"
    " с поиском подходящей вакансии в компании Latoken,"
    " расскажет о деталях работы и процессе интервью."
)


@dp.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(START_MESSAGE)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
