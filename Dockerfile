FROM --platform=linux/amd64 python:3.13-slim
LABEL maintainer="omelkov85@gmail.com"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/media
RUN mkdir -p /app/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /app/media
RUN chmod -R 755 /app/media

RUN chown -R django-user:django-user /app/static
RUN chmod -R 755 /app/static

USER django-user
