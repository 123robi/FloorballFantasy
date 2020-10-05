from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_goalkeepers.serializers import GoalkeeperSerializer
from fantasy.floorball_goalkeepers.tasks import get_goalies


class GoalkeepersListView(generics.ListAPIView):
    queryset = Goalkeeper.objects.all()
    serializer_class = GoalkeeperSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['name', 'floorball_team__name']


class GetGoalies(APIView):
    def get(self, request):
        get_goalies.delay()
        return Response("DONE")
