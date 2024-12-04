FROM python:3.8.15-alpine

WORKDIR /usr/share/app

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

COPY . /usr/share/app/

RUN apk update && \
    apk add --no-cache \
    python3-dev \
    gcc \
    libc-dev \
    mariadb-dev \
    pkgconfig

RUN pip install --upgrade pip

ADD ./requirements.txt /usr/share/app/requirements.txt

RUN pip install -r /usr/share/app/requirements.txt




