
from mfm_beheerportaal.settings import *

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': 'mfm_beheerportaal',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'todo.dbuser',
        'PASSWORD': 'todo.dbpassword',
        'HOST': 'todo.dbhost',
        'PORT': '5432',
        },
    }

# TODO: Put your real url here to configure Sentry.
# RAVEN_CONFIG = {
#     'dsn': ('http://some:hash@your.sentry.site/some_number')}

# Add your staging name here
ALLOWED_HOSTS = ['admin.multiflexmeter.net']
