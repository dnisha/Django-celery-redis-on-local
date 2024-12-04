#!/bin/sh

docker rmi -f django-celery-redis-on-local-worker1
docker rmi -f django-celery-redis-on-local-worker2
docker rmi -f django-celery-redis-on-local-app
docker rmi -f django-celery-redis-on-local-db