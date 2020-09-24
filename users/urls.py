from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

router = routers.DefaultRouter()

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('users/', views.UserViewSet.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
