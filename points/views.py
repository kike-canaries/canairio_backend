# Create your views here.
import logging

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from points.influx_settings import influx_client
from points.serializers import SensorSerializer
from util import calculate_now_cast, get_measurement_location

logger = logging.getLogger(__name__)


@api_view(['POST'])
@authentication_classes((JWTAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def save_points(request):
    """
    Saves points sent in the post body as JSON to influxDB.
    :param request:
    :return:
    """
    point_data = request.data
    try:
        for data_point in point_data:
            for key, value in data_point.get('fields').items():
                data_point['key'] = float(value)
        is_success = influx_client.write_points(point_data)
    except:
        logger.exception('Error while saving points.', extra={'extra-data': point_data})
        print(point_data)
        return Response(data={'success': False}, status=400)
    response_data = {
        'result': is_success
    }
    return Response(data=response_data, status=201)


@swagger_auto_schema(
    operation_description="Returns a list of objects for each of the registered sensors with their last reported PM "
                          "2.5 values and the time of the last report.", method='get')
@api_view(['GET'])
@authentication_classes((JWTAuthentication, BasicAuthentication))
@csrf_exempt
def get_last_point(request):
    measurements = influx_client.get_list_measurements()
    results = []
    for measurement in measurements:
        res = list(influx_client.query(
            """
            SELECT last("pm25") AS "last_pm25", time AS "time" 
            FROM "canairio"."autogen"."{}" 
            """.format(measurement['name'])
        ))
        if res:
            results.append({**measurement, **res[0][0]})

    return Response(results)


@swagger_auto_schema(
    operation_description="Returns a list of objects with NowCast values for each one of the stations currently "
                          "registered in the system. The calculation requires the station to have transmitted data "
                          "continuously for at least 12 hours. See "
                          "https://cran.r-project.org/web/packages/PWFSLSmoke/vignettes/NowCast.html for  more "
                          "information on NowCast.", method='get')
@api_view(['GET'])
@authentication_classes((JWTAuthentication, BasicAuthentication))
def get_now_cast(request):
    measurements = influx_client.get_list_measurements()
    results = []
    for measurement in measurements:
        res = list(influx_client.query(
            """
            SELECT mean("pm25") AS "mean_pm25" 
            FROM "{}"."autogen"."{}" 
            WHERE time > now() - 12h 
            GROUP BY time(1h) FILL(null)
            """.format(settings.INFLUXDB_DATABASE, measurement['name'])
        ))
        measurement['nowcast_concentration'] = calculate_now_cast(next(iter(res), None))
        measurement['location'] = get_measurement_location(measurement)
        results.append(measurement)

    return Response(results)


class SensorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = SensorSerializer

    def get_queryset(self):
        return self.request.user.sensors.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
