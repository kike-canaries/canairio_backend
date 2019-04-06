# Create your views here.
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from points.influx_settings import influx_client


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
        is_success = influx_client.write_points(point_data)
    except:
        is_success = False
    response_data = {
        'result': is_success
    }
    return Response(data=response_data, status=200)


@api_view(['GET'])
@authentication_classes((JWTAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def get_now_cast(request):
    measurements = influx_client.get_list_measurements()
    results = []
    for measurement in measurements:
        res = list(influx_client.query(
            'SELECT last("pm25") AS "last_pm25", time AS "time" FROM "canairio"."autogen"."{}"'.format(measurement['name'])
        ))
        results.append({**measurement, **res[0][0]})

    return Response(results)
