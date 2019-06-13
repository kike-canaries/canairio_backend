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

DATABASES = {
    'default': config(
        default=config('DATABASE_URL')
    )
}

django_heroku.settings(locals())
