from django.db import models
from django.db.models import DecimalField, CharField
from django.contrib.auth.models import User


class Sensor(models.Model):

    mac = CharField(max_length=12)
    lat = DecimalField(max_digits=11, decimal_places=8)
    lon = DecimalField(max_digits=11, decimal_places=8)
    name = CharField(max_length=100)
    user = models.ForeignKey(User, related_name='sensors', on_delete=models.SET_NULL, null=True)
