import datetime

import dateutil
import pytz
from influxdb import InfluxDBClient
import pprint

from canairio.settings.base import getenvvar

INFLUXDB_HOST = getenvvar('INFLUXDB_HOST')
INFLUXDB_PORT = getenvvar('INFLUXDB_PORT')
INFLUXDB_USERNAME = getenvvar('INFLUXDB_USERNAME')
INFLUXDB_PASSWORD = getenvvar('INFLUXDB_PASSWORD')
INFLUXDB_DATABASE = getenvvar('INFLUXDB_NAME')
INFLUXDB_TIMEOUT = 10

influx_client = InfluxDBClient(
    host=INFLUXDB_HOST,
    port=INFLUXDB_PORT,
    username=INFLUXDB_USERNAME,
    password=INFLUXDB_PASSWORD,
    database=INFLUXDB_DATABASE
)


measurements = influx_client.get_list_measurements()
results = []
for measurement in measurements:
    res = list(influx_client.query(
        """
        SELECT last("pm25") AS "last_pm25", time AS "time" 
        FROM "canairio"."autogen"."{}" 
        """.format(measurement['name'])
    ))
    if res and dateutil.parser.parse(res[0][0]['time']) < (datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(hours=24)):
        results.append({**measurement, **res[0][0]})

measurements = influx_client.get_list_measurements()
results = []
for measurement in measurements:
    res = list(influx_client.query(
        """
        SELECT last("aqs") AS "last_aqs", time AS "time" 
        FROM "canairio"."autogen"."{}" 
        """.format(measurement['name'])
    ))
    if res and dateutil.parser.parse(res[0][0]['time']) < (datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(hours=24)):
        results.append({**measurement, **res[0][0]})

for result in results:
    print(f"deleting {result['name']}")
    influx_client.drop_measurement(measurement=result['name'])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)
