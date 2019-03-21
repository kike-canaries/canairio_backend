from django.db import models


# Create your models here.
class Track(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
