from .base import *

ENVIRONMENT = 'production'

DEBUG = False

ALLOWED_HOSTS = ['gblabs.co']

CORS_ORIGIN_WHITELIST = ['canairiofront.herokuapp.com']

FB_API_KEY = getenvvar('FB_API_KEY', '')
FB_AUTH_DOMAIN = getenvvar('FB_AUTH_DOMAIN', '')
FB_DATABASE_URL = getenvvar('FB_DATABASE_URL', '')
FB_STORAGE_BUCKET = getenvvar('FB_STORAGE_BUCKET', '')

INFLUXDB_HOST = getenvvar('INFLUXDB_HOST', '')
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = None
INFLUXDB_PASSWORD = None
INFLUXDB_DATABASE = getenvvar('INFLUXDB_DATABASE', '')
INFLUXDB_TIMEOUT = 10

DATABASES = {
    'default': config(
        default=config('DATABASE_URL')
    )
}

SECRET_KEY = getenvvar('SECRET_KEY')
