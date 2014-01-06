from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pyend',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
    }
}
