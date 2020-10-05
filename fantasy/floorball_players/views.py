from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_players.serializer import FloorballPlayerSerializer


class PlayersListView(generics.ListAPIView):
    queryset = FloorballPlayer.objects.all()
    serializer_class = FloorballPlayerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'floorball_team__name']


class TopPlayersListView(generics.ListAPIView):
    queryset = FloorballPlayer.objects.all().order_by('-points')[:10]
    serializer_class = FloorballPlayerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
