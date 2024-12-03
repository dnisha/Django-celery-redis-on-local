FROM python:3.8.15-alpine

# RUN apk update && apk add python3-dev gcc libc-dev

RUN apk update && \
    apk add --no-cache \
    python3-dev \
    gcc \
    libc-dev \
    mariadb-dev \
    pkgconfig

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ../backend /app/backend
ADD ../backend/docker /app/docker

RUN chmod +x /app/docker/server-entrypoint.sh
RUN chmod +x /app/docker/worker-entrypoint.sh

