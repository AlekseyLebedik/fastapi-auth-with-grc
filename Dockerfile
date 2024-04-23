FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3.12 -
    
RUN pip install poetry

WORKDIR /app

RUN poetry new .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY requirements.txt .

RUN poetry add $(cat requirements-docker.txt | xargs)

COPY . .

