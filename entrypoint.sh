#!/bin/bash

gunicorn queryHelper.wsgi:application --bind 0.0.0.0:8000

#python3 manage.py runserver