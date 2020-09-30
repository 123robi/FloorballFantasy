from rest_framework import serializers

from fantasy.common.exceptions import UserAlreadyHasTeam, TeamSizeException
from fantasy.floorball_players.models import FloorballPlayer
from fantasy.teams.models import Team


class FloorballPlayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = FloorballPlayer
        fields = ('id', 'name', 'games_played', 'points', 'goals', 'assists')
        extra_kwargs = {
            'name': {'read_only': True},
            'games_played': {'read_only': True},
            'points': {'read_only': True},
            'goals': {'read_only': True},
            'assists': {'read_only': True}
        }


class TeamSerializer(serializers.ModelSerializer):
    players = FloorballPlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'players')

    def create(self, validated_data):
        if Team.objects.filter(user=validated_data['user']).count() != 0:
            raise UserAlreadyHasTeam

        players = validated_data.pop('players', [])
        if len(players) != 5:
            raise TeamSizeException

        team = Team.objects.create(**validated_data)
        for player in players:
            team.players.add(player['id'])
        return team

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs
