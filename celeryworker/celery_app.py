from celery import Celery

app = Celery('celeryworker')

# Configure Celery from the celeryconfig.py file
app.config_from_object('celeryconfig')

# Manually specify task imports
app.conf.imports = ('assignments.tasks',)  # Ensure this matches the path to your tasks.py
