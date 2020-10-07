from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_players.serializer import FloorballPlayerSerializer
from fantasy.floorball_players.tasks import set_players_initial_price


class FloorballPlayerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FloorballPlayer.objects.all()
    serializer_class = FloorballPlayerSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'floorball_team__name']

    @action(methods=['get'], detail=False)
    def top(self, request):
        return Response(
            FloorballPlayerSerializer(FloorballPlayer.objects.all().order_by('-points')[:10], many=True).data
        )

    @action(methods=['get'], detail=False)
    def get_prices(self, request):
        set_players_initial_price.delay()
        return Response('DONE')
