from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from fantasy.teams.models import Team
from fantasy.teams.serializer import TeamSerializer


class TeamViewSet(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Team.objects.all().filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeamDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            return Response(TeamSerializer(Team.objects.filter(user=request.user.id), many=True).data)
        except Team.DoesNotExist:
            return Response({'detail': "First you have to create a team!"})
