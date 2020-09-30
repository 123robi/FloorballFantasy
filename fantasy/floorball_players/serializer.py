from rest_framework import serializers

from fantasy.floorball_players.models import FloorballPlayer


class FloorballPlayerSerializer(serializers.ModelSerializer):
    floorball_team = serializers.StringRelatedField()

    class Meta:
        model = FloorballPlayer
        fields = '__all__'
