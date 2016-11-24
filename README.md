# listfully
Listfully


import os

# local_settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

ACCOUNT_ACTIVATION_DAYS = 5

REGISTRATION_OPEN = True

REGISTRATION_SALT = ''

SECRET_KEY = ''

DEBUG=True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))

ALLOWED_HOSTS=[]
