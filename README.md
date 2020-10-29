# formula-studio
A CMS for yoga and fitness studios written in Django

## Still in very early phase of development

### Installation on Linux and macOS

For installation, make sure yoy have `python3` and `pip3` installed. Clone repo

```
git clone https://github.com/mbrav/formula-studio
cd formula-studio
```

Setup a local python enviornment:
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```
pip3 install -r requirements.txt
```

Setup Django database and migrations:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Setup an admin user:
```
python3 manage.py createsuperuser
```

Run server!
```
python3 manage.py runserver
```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



