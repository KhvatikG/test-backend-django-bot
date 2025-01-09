FROM python:3.13-alpine

LABEL authors="Игорь"

WORKDIR /app

RUN apk update && \
    apk add --no-cache libpq-dev gcc curl musl-dev python3-dev postgresql-client bash

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

RUN poetry --version

RUN poetry config virtualenvs.create false

COPY ../pyproject.toml ../poetry.lock /app/

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./src /app/src
RUN echo "СКОПИРОВАННО"
# Загрузка wait-for-it
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

EXPOSE 8000
ENV PYTHONPATH="/app:${PYTHONPATH}"

COPY ./src/entrypoint.sh /app/src/entrypoint.sh
RUN chmod +x /app/src/entrypoint.sh

ENTRYPOINT ["bash", "/app/src/entrypoint.sh"]
CMD ["gunicorn", "--chdir", "/app/src", "--bind", "0.0.0.0:8000", "core.wsgi:application"]

