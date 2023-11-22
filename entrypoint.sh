#!/bin/bash

pip3 install psycopg2
pip3 install django-filter
pip3 install django-bootstrap-icons
pip3 install django-admin
pip3 install Django
pip3 install psycopg2-binary

python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn queryhelper.wsgi:application --bind 0.0.0.0:8000