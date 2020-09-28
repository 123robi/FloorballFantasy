from django.urls import path
from rest_framework import routers

from fantasy.floorball_players import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.PlayersListView.as_view()),
    path('top/', views.TopPlayersListView.as_view()),
]
