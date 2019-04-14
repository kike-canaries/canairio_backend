from rest_framework import serializers

from points.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'mac', 'lat', 'lon', 'name' )
