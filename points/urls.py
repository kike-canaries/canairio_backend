from django.urls import path
from points import views

urlpatterns = [
    path('save/', views.save_points),
]
