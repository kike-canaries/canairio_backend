from .base import *

import django_heroku

ENVIRONMENT = 'production'

DEBUG = False

ALLOWED_HOSTS = ['gblabs.co']

CORS_ORIGIN_WHITELIST = ['canairiofront.herokuapp.com']

FB_API_KEY = getenvvar('FB_API_KEY')
FB_AUTH_DOMAIN = getenvvar('FB_AUTH_DOMAIN')
FB_DATABASE_URL = getenvvar('FB_DATABASE_URL')
FB_STORAGE_BUCKET = getenvvar('FB_STORAGE_BUCKET')

SECRET_KEY = getenvvar('SECRET_KEY')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

django_heroku.settings(locals())

## This is used during development phase when testing production
# with heroku, look at
# https://github.com/kennethreitz/dj-database-url/issues/107
# Uncomment when necessary
# del DATABASES['default']['OPTIONS']['sslmode']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
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
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True
