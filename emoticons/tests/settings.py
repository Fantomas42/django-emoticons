"""Settings for testing emoticons"""

DATABASES = {
    'default': {'NAME': 'emoticons.db',
                'ENGINE': 'django.db.backends.sqlite3'}
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]

INSTALLED_APPS = [
    'emoticons',
    'django.contrib.staticfiles'
]

SECRET_KEY = 'secret-key'

STATIC_URL = '/'
