#!/bin/bash

# Прекращение выполнения скрипта при ошибке
set -e

# Ожидание базы данных
/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up!"

# Применение миграций
echo "Applying database migrations..."
python3 src/manage.py makemigrations
python3 src/manage.py migrate --noinput

echo "Creating superuser..."
python3 src/manage.py create_superuser

# Запуск сервера
echo "Starting server..."
exec "$@"
