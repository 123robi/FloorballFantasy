from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from fantasy.teams.models import Team
from fantasy.teams.serializer import TeamSerializer
from fantasy.users.premissions import IsOwner


class TeamViewSet(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Team.objects.all().filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeamDetail(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
