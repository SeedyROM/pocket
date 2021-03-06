import os

abs_path = lambda *x: os.path.abspath(*x)

BASE_DIR = abs_path(os.path.join(__file__, '../../../'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database', 'pocket.sqlite3')
    }
}

INSTALLED_APPS = ('services.auth',)

SECRET_KEY = 'REPLACE_ME'
