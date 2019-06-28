from .base import *

ENVIRONMENT = 'test'

# Please make sure that you configure in the testing environment the
# name without the _test suffix
DATABASES['default']['NAME'] = '{}_test'.format(getenvvar('DATABASE_NAME'))

TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_VERBOSE = 2
TEST_OUTPUT_DIR = 'test-results'
