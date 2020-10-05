from rest_framework import serializers

from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.serializer import FloorballTeamSerializer


class GoalkeeperSerializer(serializers.ModelSerializer):
    floorball_team = FloorballTeamSerializer(many=False, read_only=True)

    class Meta:
        model = Goalkeeper
        fields = '__all__'
