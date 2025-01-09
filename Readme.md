# TestBackEndDjangoBot

Telegram бот с регистрацией пользователей и управлением подписками на базе Django и PostgreSQL.

## Функционал

- Регистрация пользователей через Telegram
- Управление подписками
- Проверка статуса подписки
- Django админ-панель для управления пользователями и подписками

## Требования

- Docker и Docker Compose
- Telegram Bot Token

## Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd TestBackEndDjangoBot
```

2. Создайте файл `.env` в директории src:
```bash
# Данные БД
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
# Токен бота
TOKEN=your_telegram_bot_token
# Адрес бэкенда, по умолчанию http://web:8000
BACKEND_URL=http://web:8000
# Данные для админки
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@django.com
```

3. Запустите через Docker Compose в директории docker:
```bash
docker-compose up --build
```

Сервисы будут доступны:
- Django Admin: http://localhost:8000/admin
- PostgreSQL: localhost:5432

## Технический стек

- Python 3.12
- Django 5.1.4
- Aiogram 3.17.0
- PostgreSQL 17.2
- Poetry для управления зависимостями

## Зависимости

```toml
django = "^5.1.4"
djangorestframework = "^3.15.2"
psycopg2 = "^2.9.10"
gunicorn = "^23.0.0"
aiogram = "^3.17.0"
pydantic = "^2.10.4"
pydantic-settings = "^2.7.1"
requests = "^2.32.3"
```

## Команды бота

- `/start` - Начать регистрацию
- `/status` - Проверить статус подписки
- `fake_sub` - Создание подписки на месяц

## Разработка

Для локального запуска без Docker:

1. Установите зависимости:
```bash
poetry install
```

2. Примените миграции:
```bash
poetry run python src/manage.py migrate
```

3. Создайте суперпользователя:
```bash
poetry run python src/manage.py createsuperuser
```

4. Запустите сервер разработки:
```bash
poetry run python src/manage.py runserver
```

5. Запустите бота:
```bash
poetry run python bot/main.py
```

## Лицензия

[MIT License](LICENSE)