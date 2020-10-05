from rest_framework import serializers

from fantasy.floorball_players.models import FloorballPlayer
from fantasy.floorball_teams.models import FloorballTeam


class FloorballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorballTeam
        fields = ['name', 'image_url']


class FloorballPlayerSerializer(serializers.ModelSerializer):
    floorball_team = FloorballTeamSerializer(many=False, read_only=True)

    class Meta:
        model = FloorballPlayer
        fields = '__all__'
