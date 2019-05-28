from .base import *

ENVIRONMENT = 'development'
INFLUXDB_HOST = 'influxdb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'canairio',
        'USER': getenvvar('DATABASE_USERNAME'),
        'PASSWORD': getenvvar('DATABASE_PASSWORD'),
        'HOST': 'timescaledb',
        'PORT': '5432',
    },
}
