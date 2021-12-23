#!/bin/sh

set -e

echo ">>>>>>>>>>>> Current User... >>>>>>>>>>>>>"
whoami

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn sealights_assignments.wsgi:application --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=debug \
    --log-file=/var/log/gunicorn/gunicorn.log

