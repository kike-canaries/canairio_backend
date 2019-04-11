import dateutil

from points.models import Sensor


def calculate_now_cast(results):
    """
    Calculates the NowCast as per https://cran.r-project.org/web/packages/PWFSLSmoke/vignettes/NowCast.html
    :param results: List of dicts
    :return: nowcast value
    """

    if not results:
        return None

    # @todo:gustavo validate nowcast prerrequisites for missing values

    # sort hourly averages by descending date (most recent first)
    sorted_concentrations = list(map(lambda d: d['mean_pm25'],
                         sorted(results, key=lambda k: dateutil.parser.parse(k['time']), reverse=True)))

    if None in sorted_concentrations:
        return None

    min_concentration = min(sorted_concentrations)
    max_concentration = max(sorted_concentrations)

    weight = min_concentration / max_concentration

    # weight factor
    weight = 0.5 if weight < 0.5 else weight

    sum_numerator = 0
    sum_denominator = 0
    for i, c in enumerate(sorted_concentrations):
        sum_numerator += (weight**i) * c
        sum_denominator += (weight**i)

    nowcast = sum_numerator/sum_denominator

    return nowcast

def get_measurement_location(measurement):
    try:
        sensor = Sensor.objects.values_list('lat', 'lon').get(name=measurement['name'])
    except:
        return None
    return sensor
