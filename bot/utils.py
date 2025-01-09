from .config.settings import settings
import requests

from loguru import logger


async def user_register(telegram_id_: int, name: str) -> None:
    """
    Регистрация пользователя
    """
    URL = settings.BACKEND_URL + "/api/users/"

    json_data = {
        "telegram_id": telegram_id_,
        "name": name
    }
    try:
        response = requests.post(url=URL, json=json_data)
        response.raise_for_status()
    except Exception as e:
        print(f"[user_register]Логируем и поднимаем {e}")
        raise e from e
    else:
        return response.json()


async def get_user_subscribe(telegram_id_: int):
    """
    Получение подписки пользователя
    """
    logger.info(f"Получение подписки пользователя {telegram_id_}")
    user = await get_user(telegram_id_)
    logger.info(f"Получен пользователь {user}")
    if not user:
        return {"Подписка": "Отсутствует"}
    user_id = user.get("id")
    URL = settings.BACKEND_URL + "/api/subscriptions/" + str(user_id)
    logger.info(f"Получен URL {URL}")
    try:
        response = requests.get(url=URL)
        logger.info(f"Получен ответ {response.json()}")
        if response.status_code == 404:
            return {"Подписка": "Отсутствует"}
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Ошибка при получении подписки {e}")
        raise e
    else:
        return response.json()


async def get_user(telegram_id_: int):
    """
    Получение пользователя
    """
    URL = settings.BACKEND_URL + "/api/users-telegram/" + str(telegram_id_)
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
    except Exception as e:
        print(f"[get_user]Логируем и поднимаем {e}")
        raise e from e
    else:
        return response.json()


async def get_fake_subscribe(telegram_id_: int):
    """
    Оформление подписки на месяц
    """
    URL = settings.BACKEND_URL + "/api/subscriptions/"

    user = await get_user(telegram_id_)
    user_id = user.get("id")

    json_data = {
        "user": user_id,
        "duration": 30*24*60*60,
    }
    try:
        response = requests.post(url=URL, json=json_data)
        response.raise_for_status()
    except Exception as e:
        print(f"[get_fake_subscribe]Логируем и поднимаем {e}")
        raise e from e
    else:
        return response.json()