from django.urls import path
from rest_framework import routers

from fantasy.floorball_goalkeepers import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.GoalkeepersListView.as_view()),
    path('get_goalkeepers/', views.GetGoalies.as_view()),
]
