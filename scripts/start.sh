#! /bin/bash

# source .env

# apply migrations onto db
# python manage.py db upgrade

# start server
# flask run --host=0.0.0.0 --port=5000
gunicorn server:app -w 2 --threads 2 -b 0.0.0.0:5000