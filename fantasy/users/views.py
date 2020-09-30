from django.contrib.auth.models import User
from rest_framework import permissions, generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from fantasy.teams.models import Team
from fantasy.users.serializer import UserSerializer


class UserViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HasTeam(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if Team.objects.filter(user=request.user.id).count() == 1:
            return Response(True)
        else:
            return Response(False)
