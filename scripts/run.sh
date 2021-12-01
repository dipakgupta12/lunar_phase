#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser --no-input --username='admin' --email='admin@gmail.com'

whoami

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi