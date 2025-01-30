#!/bin/bash

# Wait for MySQL to be ready
# 
sleep 10

# Apply migrations
python manage.py migrate


# Collect static files
# python manage.py collectstatic --noinput

# Start Django development server
exec python manage.py runserver 0.0.0.0:8000
