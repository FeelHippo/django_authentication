#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

#    It may be useful to know which ports are open and running services on a target machine.  The -z flag can
#    be used to tell nc to report open ports, rather than initiate a connection. Usually it's useful to turn on
#    verbose output to stderr by use this option in conjunction with -v option.
#
#    For example:
#
#         $ nc -zv host.example.com 20-30
#         Connection to host.example.com 22 port [tcp/ssh] succeeded!
#         Connection to host.example.com 25 port [tcp/smtp] succeeded!

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# https://forum.djangoproject.com/t/users-customuser-does-not-exist/9951/3
# TODO: "The migration files should be part of your source being used to create the container."
echo "~~~ FLUSHING SERVER..."
python manage.py flush --no-input
echo "~~~ MAKING MIGRATIONS SERVER..."
python manage.py makemigrations
echo "~~~ MIGRATING SERVER..."
python manage.py migrate
echo "~~~ SHOWING MIGRATIONS SERVER..."
python manage.py showmigrations
echo "~~~ SERVER DONE."

exec "$@"