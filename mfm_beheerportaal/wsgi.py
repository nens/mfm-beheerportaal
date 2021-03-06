"""
WSGI config for the mfm_beheerportaal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mfm_beheerportaal.developmentsettings")
# bin/gunicorn-with-settings sets the correct dev/staging/prod settings, btw.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
