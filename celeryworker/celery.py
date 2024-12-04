from celery import Celery

app = Celery('dcelery')

app.config_from_object('celeryconfig')

