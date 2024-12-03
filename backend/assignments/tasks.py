from celery import shared_task
import time

@shared_task
def long_running_task():
    """Simulate a long-running task by using sleep."""
    print("Task started...")
    time.sleep(10)  # Simulate a long-running task (e.g., 10 seconds)
    print("Task finished!")
    return "Task complete"