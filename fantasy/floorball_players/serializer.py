from rest_framework import serializers

from fantasy.floorball_players.models import FloorballPlayer


class FloorballPlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FloorballPlayer
        fields = '__all__'
        depth = 2
