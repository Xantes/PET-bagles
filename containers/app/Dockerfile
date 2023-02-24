FROM python:3.11-slim

RUN addgroup --system bagles_app && \
    adduser --system --group bagles_app && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \ 
    curl

WORKDIR /app

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache -r requirements.txt && \
    chown bagles_app:bagles_app -R .

COPY settings/supervisord.conf /etc/

COPY settings/gunicorn.conf /etc/supervisord.d/

ENTRYPOINT [ "supervisord" ]

USER bagles_app