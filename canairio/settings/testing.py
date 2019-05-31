from .base import *

ENVIRONMENT = 'test'

# Please make sure that you configure in the testing environment the
# name without the _test suffix
DATABASES['default']['NAME'] = '{}_test'.format(getenvvar('DATABASE_NAME'))
