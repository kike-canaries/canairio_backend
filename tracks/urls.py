from django.urls import path
from tracks import views

urlpatterns = [
    path('save/', views.save_track),
    path('list/', views.list_tracks),
]
