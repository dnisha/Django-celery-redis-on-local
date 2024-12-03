from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_routes = {'newapp.tasks.*': {'queue': 'queue1'}, 'newapp.tasks.task2': {'queue': 'queue2'}}
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}
# Automatically discover tasks in all installed apps
app.autodiscover_tasks()
