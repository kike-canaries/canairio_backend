from django.conf import settings
from influxdb import InfluxDBClient

influx_client = InfluxDBClient(
    host=settings.INFLUXDB_HOST,
    port=settings.INFLUXDB_PORT,
    username=settings.INFLUXDB_USERNAME,
    password=settings.INFLUXDB_PASSWORD,
    database=settings.INFLUXDB_DATABASE
)
