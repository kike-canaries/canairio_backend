from .base import *

import django_heroku

ENVIRONMENT = 'production'

DEBUG = True

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

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

django_heroku.settings(locals())

## This is used during development phase when testing production
# with heroku, look at
# https://github.com/kennethreitz/dj-database-url/issues/107
# Uncomment when necessary
# del DATABASES['default']['OPTIONS']['sslmode']
