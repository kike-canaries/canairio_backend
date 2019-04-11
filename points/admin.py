from django.contrib import admin

# Register your models here.
from points.models import Sensor


class SensorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sensor, SensorAdmin)
