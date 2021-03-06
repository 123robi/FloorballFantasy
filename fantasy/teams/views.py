from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.models import FloorballPlayer
from fantasy.teams.models import Team
from fantasy.teams.serializer import TeamCreateSerializer, TeamRetrieveSerializer, TeamListSerializer


class TeamViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TeamCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        if self.action == 'list':
            return Team.objects.order_by('points', 'budget')
        return Team.objects.all().filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=False)
    def my_team(self, request):
        try:
            return Response(TeamRetrieveSerializer(
                Team.objects.filter(user=request.user.id).select_related('goalie__floorball_team').prefetch_related(
                    'players__floorball_team').select_related('team_attack').select_related('team_defense'),
                many=True).data)
        except Team.DoesNotExist:
            return Response({'detail': "First you have to create a team!"})

    @action(methods=['put'], detail=False)
    def update_captain(self, request):
        try:
            team = Team.objects.filter(user=request.user.id).first()
        except Team.DoesNotExist:
            return Response({'detail': "First you have to create a team!"})

        if request.data['isCaptainGoalie']:
            captain = Goalkeeper.objects.filter(id=request.data['captainId']).first()
        else:
            captain = FloorballPlayer.objects.filter(id=request.data['captainId']).first()

        team.captain_object = captain
        team.captain_object.save()
        team.save()
        return Response('Updated')
