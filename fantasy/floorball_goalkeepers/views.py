from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_goalkeepers.serializers import GoalkeeperSerializer
from fantasy.floorball_goalkeepers.tasks import get_goalies, set_goalie_initial_price


class GoalkeepersListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goalkeeper.objects.all()
    serializer_class = GoalkeeperSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'floorball_team__name']

    @action(methods=['get'], detail=False)
    def get_goalkeepers_celery(self, request):
        get_goalies.delay()
        return Response("DONE")

    @action(methods=['get'], detail=False)
    def get_goalkeepers_initial_price_celery(self, request):
        set_goalie_initial_price.delay()
        return Response("DONE")
