from django.urls import path
from rest_framework import routers

from fantasy.teams import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.TeamViewSet.as_view()),
    path('my_team/', views.TeamDetail.as_view()),
]
