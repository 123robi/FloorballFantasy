from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'auth/$', obtain_auth_token),
    url(r'^', include(router.urls)),
]
