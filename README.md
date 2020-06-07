#Django Blog Application

##Make virtualenv

On Linux:

>$ python3.6 -m venv 

>$ . venv/bin/

On Windows


> python -m venv venv

> venv/Scripts/activate

(venv)$ pip install -r requirements.

##migrate

>(venv)$ cd myproject

>(venv)$ python manage.py migrate

##Make admin user

>(venv)$ python manage.py createsuperuser

##runserver

>(venv)$ cd myproject

(venv)$ python manage.py 

