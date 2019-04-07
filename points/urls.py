from django.urls import path
from points import views

urlpatterns = [
    path('save/', views.save_points),
    path('get/', views.get_last_point),
    path('get/nowcast', views.get_now_cast),
]
