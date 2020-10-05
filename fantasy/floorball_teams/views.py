from rest_framework import filters, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from fantasy.floorball_teams.models import FloorballTeam
from fantasy.floorball_teams.serializer import FloorballTeamSerializer


class TeamsListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FloorballTeam.objects.all()
    serializer_class = FloorballTeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
