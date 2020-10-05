from rest_framework import serializers

from fantasy.common.exceptions import UserAlreadyHasTeam

from fantasy.teams.models import Team


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'players', 'goalie')

    def create(self, validated_data):
        if Team.objects.filter(user=validated_data['user']).count() != 0:
            raise UserAlreadyHasTeam

        return super().create(validated_data)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs


class TeamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['user']
        depth = 2
