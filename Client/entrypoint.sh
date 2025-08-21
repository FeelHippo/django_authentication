#!/bin/sh

echo "~~~ FLUSHING CLIENT..."
python manage.py flush --no-input
echo "~~~ MIGRATING CLIENT..."
python manage.py migrate
echo "~~~ CLIENT DONE."