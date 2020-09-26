from django.urls import path
from rest_framework import routers

from fantasy.floorball_teams import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index, name='index'),
]
