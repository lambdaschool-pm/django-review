# How to deploy a django app on Heroku
## 1. Sign up for a free [heroku account](https://www.heroku.com/)

## 2. Install a Heroku CLI
  * [ ] check if you already have a cli by tpying ```heroku --version```
   you should get something like ***heroku/7.12.6 darwin-x64 node-v10.9.0***
   * [ ] if you dont have the heroku cli, install it using one of the methods on the [installation page](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

   and then again type ```heroku --version``` in your terminal

## 3. Login into heroku using your terminal by typing ```heroku login```
It will ask for your login credential. If you are successfull, it will tell you that logged in as .......

## 4. Get your app ready
* [ ] If you dont have a django app, make one. We will be using github, so, make sure your app lives in a git repository. But am assuming that you have one settup and have been making frequent commits, so lets start the deployment. Other deployment options can be found [here](https://devcenter.heroku.com/categories/deployment).
* [ ] You should have install python-decouple by now, if not `pipenv install python-decouple` - set important/secret values as environment variables.
* [ ] You should have an `.env` file, if not create one
    In the `.env` type
    1. ALLOWED_HOSTS=localhost,127.0.0.1,localhost:3000,.herokuapp.com
    **2. DATABASE_URL="sqlite:///db.sqlite3"** We will let heroku do this, but this is were you can tell it where the datable will live

    3. SECRET_KEY="YOUR SECRET KEY GOES HERE"
    - you can generate a secret key by
    ```python
    import random
    '.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]) # All one line!
    ```
    4. DEBUG=True

* [ ]  Install new dependencies:
    1. `pipenv install gunicorn` - the webserver for Heroku to use (rather than the one built-in to Django) [link](https://github.com/benoitc/gunicorn)
    2. `pipenv install psycopg2-binary` - PostgreSQL client binaries [link](https://pypi.org/project/psycopg2-binary/)
    3. `pipenv install dj-database-url` - enables parameterizing the database connection (so Heroku uses PostgreSQL but local is still SQLite) [link](https://github.com/kennethreitz/dj-database-url)

    4. `pipenv install whitenoise` - optimizes deployment of static files (you may not have any, but it's good to add this now)
    - [Web link](http://whitenoise.evans.io/en/stable/)
    - [github link](https://github.com/evansd/whitenoise)

    5. If using `virtualenv`, you need to create a `requirements.txt` file in your project root directory with the command: `pip freeze > requirements.txt`
* [ ] In your project ```settings.py```
  - import config from decouple and dj_database_url
  ```python
  from decouple import config
  import dj_database_url
  ```

  - Use the config to bring in the ALLOWED_HOST, SECRET_KEY and DEBUG and DATABASES

  ```python
  # ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
  #OR
  ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

  SECRET_KEY = config("SECRET_KEY")

  DEBUG = config('DEBUG', cast=bool)

  DATABASES = {
    'default': dj_database_url.config('DATABASE_URL', default='sqlite:///db.sqlite3')
    }
  ```

* [ ] Configure whitenoise in your ```settings.py```

  put the middleware above all other middleware except for django security

  ```python
    MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
  ]
  ```

  Near the static area put the following lines. And if you setup the STATIC_ROOT, you will have to setup a folder

  ```python
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```

* [ ] Make a Procfile in the main directory and type in your project name to tell heroku what to run

  ```Procfile
  web: gunicorn djorg.wsgi
  ```

## 5. Deployment using [git](https://devcenter.heroku.com/articles/git#deploying-code)
* [ ] Make sure you are login into heroku ```heroku auth:whoami ```. It should display your username

* [ ] git add, commit and push all your changes to github

* [ ] create the app (app name must be unique) on heroku by typing ```heroku create YOUR_APP_NAME_GOES_HERE``` If you don't give it a name, heroku will give your app a randomly generated name.

*The app has been created and can be accessed from the url, now you have to set up the PostgreSQL, DB and configurations*
* [ ] Add a PostgreSQL by ```heroku addons:create heroku-postgresql:hobby-dev```  - makes a PostgreSQL database associated with the project (and sets the `DATABASE_URL` Heroku config var, equivalent to a local environment variable)

* [ ] Install the config plugin by typing ```heroku plugins:install heroku-config``` Will help with push up environment variables

* [ ] push your config files to heroku ```heroku config:push -a YOUR_APP_NAME_GOES_HERE```. You should get a success message. ```Successfully wrote settings to Heroku!```
Your can check that the configurations have been send out by typing ```heroku config```
*You can also create the config variables in the dashboard itself*

## 6. FINAL COMMITS, PUSH TO GITHUB and then type ```git push heroku master```
*The magic begins. Your apply will be push to heroku. Your Procfile lets heroku know which language you are using node, python and will make necessary moves.*

*to run commands on heroku, you will be typing ```heroku run python manage.py COMMAND_AFTERWARDS```*

* [ ] Run ```heroku run python manage.py migrate``` to migrate
and
* [ ] Create a super user by running ```heroku run python manage.py createsuperuser```

*other commands are `heroku run python manage.py shell` and `heroku run python manage.py dbshell`.*

* [ ] debug your code by running ```heroku logs```
[Link to the heroku error codes](https://devcenter.heroku.com/articles/error-codes)

***good luck with your deployment**
