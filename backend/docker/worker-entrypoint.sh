#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A backend worker --loglevel=info -Q queue1 --concurrency 1 -E &

# Start Flower UI (assuming it's installed and you want to run it on port 5555)
celery -A backend flower --port=5555 --address=0.0.0.0 &

# Wait for both processes to run in the background
wait
