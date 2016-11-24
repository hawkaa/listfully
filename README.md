# listfully
Listfully


# Installation instructions
Ensure to have all of these packages installed (with `pip install`):
```
django
django-registration
Pillow
```

Then create a file `listfully/local_settings.py` with the following setting keys:

```
import os

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
```

Change the values in `local_settings.py` according to your current setup.

Run database migrations:

```
$ python manage.py migrate
```

Install node dependencies:
```
$ cd static/
$ npm install 
$ cd ..

```

Run the server using the following command:
```
$ python manage.py runserver
```

Open your favourite browser and go to `http://127.0.0.1:8000/`. Enjoy!
