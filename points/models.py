from django.db import models
from django.db.models import DecimalField, CharField


class Sensor(models.Model):

    mac = CharField(max_length=12)
    lat = DecimalField(max_digits=11, decimal_places=8)
    lon = DecimalField(max_digits=11, decimal_places=8)
    name = CharField(max_length=100)
