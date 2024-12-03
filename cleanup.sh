#!/bin/sh

docker rmi -f django-celery-redis-on-local-worker
docker rmi -f django-celery-redis-on-local-app
docker rmi -f django-celery-redis-on-local-db