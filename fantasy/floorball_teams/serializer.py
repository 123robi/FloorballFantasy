from rest_framework import serializers

from fantasy.floorball_teams.models import FloorballTeam


class FloorballTeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)

    class Meta:
        model = FloorballTeam
        fields = '__all__'
