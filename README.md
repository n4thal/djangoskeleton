# Personal Branding Website

This is a Personal Branding - Website created using Django Web Framework.

## Features

* Landing Page
* Blog
* Projects
* Comments
* Redis Caching
* Header & Footer
* Blog-RSS Feed
* CMS within the Admin Panel

## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.8.3
+ Redis Server
+ Git 
+ pip
+ Virtualenv (or virtualenvwrapper)

## Requirements

+ asgiref==3.2.10
+ Django==3.0.8
+ django-redis==4.12.1
+ django-crispy-forms==1.9.2
+ redis==3.5.3
+ sqlparse==0.3.1
+ pytz==2020.1
+ django-summernote==0.8.11.6

## Install Redis Server

[Redis Quick Start](https://redis.io/topics/quickstart)

Run Redis server
```bash
redis-server
```

## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv -p python3 {{project_name}}   # create and activate environment
workon {{project_name}}   # reactivate existing environment
```

Clone GitHub Project,
```bash
git@github.com:n4thal/djangoskeleton.git

cd djangoskeleton
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Initialize Migrations
```bash
python manage.py makemigrations
```

Migrate Database,
```bash
python manage.py migrate
```

Create Superuser,
```bash
python manage.py createsuperuser
```

Set environmental variables,
```bash
os.environ['SECRET_KEY']='your very secret key here'
```
In PyCharm:
Edit the config of the manage.py run and add your key there.
https://i.stack.imgur.com/jwpVo.png
Also add the parameter
```bash
runserver
```

Run the web application via the newly created config in PyCharm or locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Add Content at: url/admin (login with previously created superuser account)

Enjoy!

# MAKE SURE TO CHANGE BEFORE PRODUCTION:

 * set DEBUG in skeleton/settings.py to False
 * probably move to a more stable DB