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


echo "~~~ FLUSHING..."
python manage.py flush --no-input
echo "~~~ MIGRATING..."
python manage.py migrate
echo "~~~ DONE..."

exec "$@"