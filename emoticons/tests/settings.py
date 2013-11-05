"""Settings for testing emoticons"""

DATABASES = {'default': {'NAME': 'emoticons.db',
                         'ENGINE': 'django.db.backends.sqlite3'}}

SECRET_KEY = 'secret-key'

STATIC_URL = '/'

INSTALLED_APPS = ['emoticons',
                  'django.contrib.staticfiles']
