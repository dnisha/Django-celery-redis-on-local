import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_routes = {'assignments.tasks.task1': {'queue': 'queue1'}, 'assignments.tasks.task2': {'queue': 'queue2'}}

app.autodiscover_tasks()