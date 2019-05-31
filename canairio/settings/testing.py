from .base import *

ENVIRONMENT = 'test'
INFLUXDB_HOST = 'influxdb'
DATABASE_HOSTNAME = getenvvar('POSTGRESQL_HOST')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'canairio_test',
        'USER': getenvvar('DATABASE_USERNAME'),
        'PASSWORD': getenvvar('DATABASE_PASSWORD'),
        'HOST': DATABASE_HOSTNAME,
        'PORT': '5432',
    },
}
