
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

# Add your staging name here
ALLOWED_HOSTS = ['admin.multiflexmeter.net']
