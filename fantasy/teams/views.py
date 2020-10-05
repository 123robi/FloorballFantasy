from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fantasy.teams.models import Team
from fantasy.teams.serializer import TeamCreateSerializer, TeamRetrieveSerializer


class TeamViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = TeamCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Team.objects.all().filter(user=self.request.user)

    @action(methods=['get'], detail=False)
    def my_team(self, request):
        try:
            return Response(TeamRetrieveSerializer(
                Team.objects.filter(user=request.user.id).select_related('goalie__floorball_team').prefetch_related(
                    'players__floorball_team'), many=True).data)
        except Team.DoesNotExist:
            return Response({'detail': "First you have to create a team!"})
