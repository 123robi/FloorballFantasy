from django.urls import path, include
from rest_framework import routers

from fantasy.teams import views

router = routers.DefaultRouter()

router.register('teams', views.TeamViewSet, basename='teams')
urlpatterns = [
    path('', include(router.urls)),
]
