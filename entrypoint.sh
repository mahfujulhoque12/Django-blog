#!/bin/sh

set -e

# Wait for database running:
sleep 5
while [[ $(nc -z $db_host 5432 &> /dev/null; echo $?) -ne 0 ]]; do echo pod is not running;sleep 3; done

python manage.py migrate
python manage.py collectstatic --noinput

python manage.py compilemessages -l en
python manage.py compilemessages -l de
python manage.py compilemessages -l ja


gunicorn matplus.wsgi:application --bind :80
