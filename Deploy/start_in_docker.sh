#!/usr/bin/env bash

set -e
set -u

export DJANGO_SETTINGS_MODULE=Project.production_settings

cd /opt/app
yarn install
gulp copy
python3 manage.py migrate --noinput        # Apply database migrations
python3 manage.py collectstatic --noinput  # Collect static files
python3 manage.py createdefaultuser   # Create default user admin
mkdir -p media/products && cp -rf fixtures/products media   # Create default user admin
python3 manage.py loaddata fixtures/category.json

supervisord -c /opt/app/Deploy/supervisor.conf
