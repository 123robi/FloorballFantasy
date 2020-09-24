from django.urls import path
from rest_framework import routers

from teams import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.TeamViewSet.as_view()),
    path('<int:pk>/', views.TeamDetail.as_view()),
]
