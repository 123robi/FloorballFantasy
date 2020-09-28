from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from fantasy.floorball_teams.models import FloorballTeam
from fantasy.floorball_teams.serializer import FloorballTeamSerializer


class TeamsListView(generics.ListAPIView):
    queryset = FloorballTeam.objects.all()
    serializer_class = FloorballTeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
