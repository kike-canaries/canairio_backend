from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):

    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='tracks', on_delete=models.SET_NULL, null=True)
