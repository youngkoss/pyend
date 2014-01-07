"""
WSGI config for deploying hcar project on heroku service
"""


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_heroku")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
