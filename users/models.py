from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True)
