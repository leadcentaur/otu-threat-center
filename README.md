


#  [Ontario Tech](https://twitter.com/ontariotech_u?lang=en) Threat center 🎯 

The Ontario Tech Vulnerability reporting system. contributions are welcome :) 

<p align="center">
  <img src="https://github.com/leadcentaur/otu-threat-center/blob/ebec59ad22884f40ca018d4094b6a68bc33f6a56/banner.JPG">
</p>

## Requirements 

- Pillow>=8.1.1
- Django>=3.1.5
- django-crispy-forms>=1.11.0
- python-social-auth==0.3.6
- social-auth-app-django>=4.0.0
- django-chartjs>=2.2.1 
- django-jsignature>=0.10

## Creating a virtual environment and installing required packages

Create a new virtual environment 
```
python3 -m venv path/to/venv
```
Enter the environment
```
source path/to/venv/bin/activate
```
Install required packages
```
pip install -r requirements.txt
```

## Setting Required Enviroment Variables
1. SECRET_KEY: The secret key used by django
2. GOOGLE_AUTH_KEY: Google OAUTH
3. GOOGLE_SECRET: Google OAUTH
4. EMAIL_HOST_USER: Username for the account which will send legal agreement emails
5. EMAIL_HOST_PASSWORD: Password for the account which will send legal agreement emails

## Setup
To setup the project in a local environment run the following commands:

1. Run the server to create the db.sqlite3 file
```
python manage.py runserver
```
* Apply initial migrations
```
python manage.py migrate --run-syncdb
```
* Create a django super user
```
python manage.py createsuperuser
```
* Run the server
```
python manage.py runserver
```

### Useful commands
* python manage.py sqlflush
* python mange.py migrate <model_name>
* python manage.py showmigrations

### Option Enviroment Variables
1. VPN_PASSWORD_LENGTH: Password length for the VPN model (default 12)
2. VPN_USERID_LENGTH: UserID length for the VPN model (default 9)
3. MAX_MESSAGE_IMAGES: Max number of images per report message thread (default 25)
4. MAX_MESSAGE_IMAGE_SIZE: Max size of message images (in bytes) (default 5MB)
5. VALID_MESSAGE_IMAGE_TYPES: Valid message image types as a string (default 'jpeg, jpg, png')
6. TAG_NEW_MESSAGES: Whether or not to display a 'new' tag on message threads a user has yet to responde to (boolean 0 or 1) (default 1) 
