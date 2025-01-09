import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from bot.config.settings import settings
from bot.utils import user_register, get_user_subscribe, get_fake_subscribe

TOKEN = settings.TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!\n"
                         f"Для продолжения зарегистрируйтесь.\n"
                         f"Введите 'reg Ваше Имя' для регистрации")


@dp.message(F.text.lower().startswith("reg"))
async def reg_handler(message: Message) -> None:
    try:
        await user_register(
            telegram_id_=message.from_user.id,
            name=message.text.split(" ")[1],
        )
    except Exception as e:
        await message.answer(f"Ошибка регистрации: {e}")
    else:
        await message.answer(f"Регистрация прошла успешно!")


@dp.message(F.text.lower() == "fake_sub")
async def reg_handler(message: Message) -> None:
    try:
        await get_fake_subscribe(
            telegram_id_=message.from_user.id,
        )
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
    else:
        await message.answer(f"Подписка оформлена успешно!")


@dp.message(F.text == "/status")
async def status_handler(message: Message) -> None:
    """
    Проверка статуса подписки
    """
    logger.info("Получена команда, получение статуса подписки")
    try:
        subscribe = await get_user_subscribe(message.from_user.id)
        if subscribe.get("start_date"):
            await message.answer(f"Подписка:\n"
                                 f"Дата начала: {subscribe.get('start_date')}\n"
                                 f"Продолжительность: {subscribe.get('duration')}\n"
                                 f"Дата окончания: {subscribe.get('end_date')}\n")
        else:
            await message.answer(f"Вы не подписаны")

    except Exception as e:
        logger.exception("Ошибка получения статуса подписки:\n")
        await message.answer(f"Ошибка: {e}")


async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
