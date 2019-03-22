# Base Django settings, suitable for production.
# Imported (and partly overridden) by developmentsettings.py which also
# imports localsettings.py (which isn't stored in svn).  Buildout takes care
# of using the correct one.
# So: "DEBUG = TRUE" goes into developmentsettings.py and per-developer
# database ports go into localsettings.py.  May your hear turn purple if you
# ever put personal settings into this file or into developmentsettings.py!

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# In older projects, this setting is called BUILDOUT_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Set up logging. No console logging. By default, var/log/django.log and
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(name)s %(levelname)s\n    %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'var', 'log', 'django.log'),
        },
        'sqllogfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'var', 'log', 'sql.log'),
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['null'],
            # Quiet by default! You can set it to ``['sqllogfile']``, which is
            # done in the development settings.
            'propagate': False,
            'level': 'DEBUG',
        },
        'factory': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',  # Suppress the huge output in tests
        },
        'django.request': {
            'handlers': ['console', 'logfile'],
            'propagate': False,
            'level': 'ERROR',  # WARN also shows 404 errors
        },
    }
}

# Production, so DEBUG is False. developmentsettings.py sets it to True.
DEBUG = False

# Override this in your own "localproductionsettings.py" file
DATABASES = {
    'default': {
        'NAME': 'beheerportaal',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'beheerportaal',
        'PASSWORD': 'beheerportaal',
        'HOST': 'localhost',
        'PORT': '5432',
        }
    }

WSGI_APPLICATION = 'mfm_beheerportaal.wsgi.application'

# Almost always set to 1.  Django allows multiple sites in one database.
SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems.  If running in a Windows
# environment this must be set to the same as your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'
# For at-runtime language switching.  Note: they're shown in reverse order in
# the interface!
LANGUAGES = (
    ('en', 'English'),
    # ('nl', 'Nederlands'),
)
# If you set this to False, Django will make some optimizations so as not to
# load the internationalization machinery.
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute path to the directory that holds user-uploaded media.
MEDIA_ROOT = os.path.join(BASE_DIR, 'var', 'media')
# Absolute path to the directory where
# "python manage.py collectstatic" places all collected static files from all
# applications' /media directory.
STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/media/'
# URL for the per-application /media static files collected by
# django-staticfiles.
STATIC_URL = '/static_media/'

# Override this in your own "localproductionsettings.py" file
# Make this unique, and don't share it with anybody.
SECRET_KEY = "y2ru!xw*hdw^qpj!k*)ct(8v503q)yn2&c3ps*7#iz^poo(6#k"

ROOT_URLCONF = 'mfm_beheerportaal.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

CACHES = {
    'default': {
        'KEY_PREFIX': BASE_DIR,
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = (
    # Below is the default list, don't modify it.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

INSTALLED_APPS = (
    'django_extensions',
    'mfm_beheerportaal',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'gunicorn',
)


CELERY_RESULT_BACKEND = 'django-db'

INSTALLED_APPS += (
    'django_celery_results',
)

# Add your production name here
ALLOWED_HOSTS = ['admin.multiflexmeter.net']

try:
    from mfm_beheerportaal.localproductionsettings import *
    # For local production overrides (DB passwords, for instance)
except ImportError:
    pass
