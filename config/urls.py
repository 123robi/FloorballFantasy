"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from fantasy.teams.urls import router as team_router
from fantasy.users.urls import router as user_router
from fantasy.floorball_teams.urls import router as floorball_team_router
from fantasy.floorball_players.urls import router as floorball_player_router
from fantasy.floorball_goalkeepers.urls import router as floorball_goalie_router

router = routers.DefaultRouter()
router.registry.extend(team_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(floorball_team_router.registry)
router.registry.extend(floorball_player_router.registry)
router.registry.extend(floorball_goalie_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
