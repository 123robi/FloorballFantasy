from django.contrib.auth.models import User
from rest_framework import permissions, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fantasy.teams.models import Team
from fantasy.users.serializer import UserSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def get_permissions(self):
        if self.action == 'has_team':
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    @action(methods=['get'], detail=False)
    def has_team(self, request):
        self.permission_classes = (IsAuthenticated,)
        if Team.objects.filter(user=request.user.id).count() == 1:
            return Response(True)
        else:
            return Response(False)
