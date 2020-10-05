from rest_framework import routers

from fantasy.floorball_goalkeepers import views

router = routers.DefaultRouter()

router.register('floorball_goalies', views.GoalkeepersListView, basename='floorball_goalies')
