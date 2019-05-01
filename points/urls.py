from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from points import views
from points.views import SensorViewSet

router = routers.DefaultRouter()
router.register('sensors', SensorViewSet, 'sensors')

urlpatterns = [
    url('^', include(router.urls)),
    path('save/', views.save_points, name='save-measure'),
    path('get/', views.get_last_point, name='latest-measure'),
    path('get/nowcast', views.get_now_cast, name='get-now-cast'),
]
