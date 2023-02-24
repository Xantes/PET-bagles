# Этап, на котором выполняются подготовительные действия
FROM python:3.11-slim as builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

RUN addgroup --system bagles_app && adduser --system --group bagles_app

USER bagles_app

COPY . .

COPY settings/supervisord.conf /etc/

COPY settings/gunicorn.conf /etc/supervisord.d/

ENTRYPOINT [ "supervisord" ]