from rest_framework import routers

from fantasy.floorball_players import views

router = routers.DefaultRouter()

router.register('floorball_players', views.FloorballPlayerViewSet, basename='floorball_players')
