[Server Client Oauth2.0 Tutorial](https://raphaelyancey.fr/en/2018/05/28/setting-up-django-oauth2-server-client.html)
    - [Repository](https://github.com/raphaelyancey/django-oauth2-example)
[How to setup Postgresql](https://gist.github.com/NickMcSweeney/3444ce99209ee9bd9393ae6ab48599d8)
[Create database from command line](https://stackoverflow.com/a/30642050/10708345)
[Setup Postgres on Docker Compose](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

### Commands
- start Django app: `cd Server` and `sudo python manage.py runserver`
- build image: `sudo docker-compose build`
- start image: / run the container: `sudo docker-compose up -d`
- check on status: `sudo docker-compose ps`
- check Django version: `python -c "import django; print(django.get_version())"`
- check on package version: `python -c "import psycopg2; print(psycopg2.__version__)"`
- check on Postgre version: `pg_config --version`
- check running images: `sudo docker ps -a`
- check error logs: `docker-compose logs -f`
- check PostgreSql tables were created in Django: `sudo docker-compose exec db psql --username=feelhippo --dbname=auth` => prompt `\l`
- ... or `sudo docker volume inspect authentication_api_postgres_data`
- migrate: `cd Server` and `sudo python manage.py migrate`

### Start
```terminaloutput
sudo docker-compose build
sudo docker-compose up -d
```