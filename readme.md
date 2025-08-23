[Server Client Oauth2.0 Tutorial](https://raphaelyancey.fr/en/2018/05/28/setting-up-django-oauth2-server-client.html)
    - [Repository](https://github.com/raphaelyancey/django-oauth2-example)
[How to setup Postgresql](https://gist.github.com/NickMcSweeney/3444ce99209ee9bd9393ae6ab48599d8)
[Create database from command line](https://stackoverflow.com/a/30642050/10708345)
[Setup Postgres on Docker Compose](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
[Install libraries](https://stackoverflow.com/a/75722775/10708345)
[Oauth2 with storage](https://codezup.com/implementing-oauth2-authentication-django-guide/) (it's pretty bad, but a good start)
[TokenAuthentication docs](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

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
### Issues
- [ModuleNotFoundError: No module named 'oauth2_provider](https://github.com/django-oauth/django-oauth-toolkit/issues/811)

### Walk Through
```terminaloutput
sudo systemctl start docker
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose logs -f
```
Once the above all works, create a superuser:
- `sudo docker-compose exec client python manage.py createsuperuser`
- `sudo docker-compose exec server python manage.py createsuperuser`

Register the client on the server:
- [tutorial from the docs](https://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html#scenario)
- `http://localhost:8000/o/applications/register/`
  - username: `root` (default from creating a superuser)
  - name: `Custom OAuth2 Provider`
  - client id: `mt7DNDsslyj8YiVARmkoqoMuhoouhc5T8Fpco1vN`
  - client secret: `XiGVuNyyOVnTryzA1SlvGt1wt661P3RvTlnQ1Z7aCOubdTAk3rrA50joB8B0aZuHlawDTzHz9WYlkM1ZOdgkONyMvBzvrPRz66VFUqmqod9syNEaqd6O3bGQ2JFZfLGH`
  - Hash client secret NOT checked (might want to use OIDC or check JWT signature later)
  - Client type: `confidential`
  - Authorization Grant Type; `Authorization Code`
  - Redirect URIs: `http://localhost:9988/customprovider/login/callback/`
  - Allowed origins: `http://localhost:3000`

Setup the Client:
- `http://localhost:9988/admin/socialaccount/socialapp/add/`
  - Make sure the custom provider is selected in the drop down menu
  - provider ID: `customprovider`
  - provider Name: `Custom OAuth2 Provider`
  - client id and client server: see above, they are registered on the server at this point
  - bottom: from the `available sites`, move `example.com` to the right

Testing: `http://localhost:3000/accounts/profile`
the server will allow our client app to request whatever it needs to authenticate its users against its database

### Run locally
- in Server/server/settings.py -> DATABASES.default -> remove HOST and PORT
- TODO: improve this, refactor
- use the virtual environment!
```terminaloutput
    source venv/bin/activate
    [if necessary]: pip install <dep-name-here>
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 8080
```