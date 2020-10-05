from rest_framework import routers

from fantasy.users import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='users_register')
