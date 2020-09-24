from django.urls import path
from rest_framework import routers

from users import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.UserViewSet.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]
