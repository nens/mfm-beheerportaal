from mfm_beheerportaal.settings import *

DEBUG = True

LOGGING['loggers']['']['level'] = 'DEBUG'
LOGGING['loggers']['django.db.backends']['handlers'] = ['sqllogfile']

DATABASES = {
    'default': {
        'NAME': 'mfm_beheerportaal',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'nens',
        'PASSWORD': 'nens',
        'HOST': 'db',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['localhost']

try:
    from mfm_beheerportaal.localsettings import *
    # For local dev overrides.
except ImportError:
    pass
