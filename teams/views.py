from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from teams.models import Team
from teams.serializer import TeamSerializer
from users.premissions import IsOwner


class TeamViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Team.objects.all().filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TeamDetail(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
