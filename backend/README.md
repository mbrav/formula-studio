## Backend Installation

### On Linux and macOS

For installation, make sure yoy have `python3` and `pip3` installed. Clone repo

-   [ ] TODO: Update these instruction using the newer `.env` method

```
$ git clone https://github.com/mbrav/formula-studio
cd formula-studio
```

Setup a local python environment:

```
$ python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
$ pip3 install -r requirements.txt
```

Setup Django database and migrations:

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Setup an admin user:

```
$ python3 manage.py createsuperuser
```

Run server

```
$ python3 manage.py runserver
```

Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Celery notes

### 1. Celery worker instance

To start the worker do `celery -A App worker --pool=solo -l info -E` where `-l info -E` is for loging purposes and should not be used in production.

### 2. Celery beat instance worker

As [expalined here](https://github.com/celery/celery/issues/2059#issuecomment-44519976), this is the actual instance that pull tasks from `celery.py`, or from schedules database table configured using the `django_celery_beat` plugin. To start the worker that executes schedules from the code:

```
celery -A App beat
```

To start the worker that executes schedules the database:

```
celery -A App beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Coverage notes

Create coverage file:

-   `coverage run --source='App,api,formula_studio' manage.py test -v 2`

Create report:

-   `coverage report`

Coverage html report:

-   `coverage html`

## Dump fixtures 

To dump data: 

- `python manage.py dumpdata formula_studio --indent 4 > formula_studio/fixtures/formula_studio.json`

To load data: 

- `python manage.py loaddata formula_studio/fixtures/model_name.json --app formula_studio`


## Development

This project is in still in alpha phase of development and goals will be fully established before the beta release.

Django admin interface in [alpha version](https://github.com/mbrav/formula-studio/releases/tag/alpha):
![](https://i.imgur.com/9w7qojU.png)

Database Model structure in [alpha version](https://github.com/mbrav/formula-studio/releases/tag/alpha):
![](https://i.imgur.com/r57wa1O.png)

### Contributing

If you've found a bug, add a feature or improve formula-studio and think it is useful then please consider contributing. Patches, pull requests or just suggestions are always welcome!

-   Source code: https://github.com/mbrav/formula-studio

-   Bug tracker: https://github.com/mbrav/formula-studio/issues

-   Project board manager: https://github.com/mbrav/formula-studio/projects/1

-   Lastly, if you found this project helpful and practical, please leave some feedback!
