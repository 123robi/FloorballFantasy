from rest_framework import routers

from fantasy.floorball_teams import views

router = routers.DefaultRouter()
router.register('floorball_teams', views.TeamsListView, basename='floorball_teams')
