FROM python:3.13-alpine

LABEL authors="Игорь"

WORKDIR /app

RUN apk update && \
    apk add --no-cache libpq-dev gcc curl musl-dev python3-dev postgresql-client

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

RUN poetry --version

RUN poetry config virtualenvs.create false

COPY ../pyproject.toml ../poetry.lock /app/

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./bot ./bot

ENV PYTHONPATH="/app:${PYTHONPATH}"

CMD ["python3", "/app/bot/main.py"]

