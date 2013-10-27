"""Settings for testing smileys"""

DATABASES = {'default': {'NAME': 'smileys.db',
                         'ENGINE': 'django.db.backends.sqlite3'}}

SECRET_KEY = 'secret-key'

INSTALLED_APPS = ['smileys']
