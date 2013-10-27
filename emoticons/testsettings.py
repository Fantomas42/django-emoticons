"""Settings for testing emoticons"""

DATABASES = {'default': {'NAME': 'emoticons.db',
                         'ENGINE': 'django.db.backends.sqlite3'}}

SECRET_KEY = 'secret-key'

INSTALLED_APPS = ['emoticons']
