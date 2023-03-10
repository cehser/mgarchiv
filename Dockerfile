# syntax=docker/dockerfile:1
FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput
