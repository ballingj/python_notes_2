### install venv
```sh
sudo apt install python3.10-venv
```
### Creat virtual environment in a folder ./venv
```sh
python -m venv ./venv
```
### activate  -- you should see (venv) in prompt
```sh
source ./venv/bin/activate
```
### deactivate  -- you should see (venv) go away
```sh
deactivate
```
### install the pip package you need
```sh
pip install django
```

### Alternative package for virtual environment
>create a virtual environment: install a package that allows to create a virtual environment
```sh
pip install virtualenv
```
>  now create a virtual environment with command `virtualenv <name>` : here we are naming it `env`
>  this will create a new folder after the name you provided
```sh
virtualenv env
```
### Activate the virtual environment
>you should see (env) in the front of prompt
```sh
source ./env/bin/activate
```
### Activate for Windows
```sh
env\scripts\activate
```
### Deactivate
```sh
deactivate
```
#### Deactivate for Windows
```sh
env\scripts\deactivate
```

### Install Django 
```sh
pip install django
```
> NOTE:  Install packages while in the virtual environment to avoid installing in global settings

# More Commands

### general help
```sh
django-admin help
```
### start a project
```sh
django-admin startproject <name_of_project>
```

### Ex:  start a project 'btre' in current directory
```sh
django-admin startproject btre .   
```
### run server
```sh
python manage.py runserver
```

### fix linter pylint if not installed
shift + ctrl + 'p'  > select interpreter for env
```sh
install pylint
```
### add the first app in current project
```sh
python manage.py startapp <name_of_app>
```
### Ex: add "pages" app in btre
```sh
python manage.py startapp projects
```

> Note: Required step everytime you add an app:
- Go to settings.py in main project and add the new app 
- Add the class name included in the Apps.py in the INSTALLED_APPS list

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',
]
```