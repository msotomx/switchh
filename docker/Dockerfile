FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Instalar deps primero para cachear capas
COPY requirements.txt /opt/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto
COPY . /opt/app

# (Opcional) Puedes hacer collectstatic en build, pero prefiero hacerlo en runtime:
# RUN python manage.py collectstatic --noinput
