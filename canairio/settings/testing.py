from .base import *

ENVIRONMENT = 'test'
INFLUXDB_HOST = 'influxdb'
try:
    DATABASE_HOSTNAME = getenvvar('DATABASE_HOSTNAME')
except:
    DATABASE_HOSTNAME = 'timescaledb'

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
