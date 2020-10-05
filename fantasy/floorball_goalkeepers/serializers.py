from rest_framework import serializers

from fantasy.floorball_goalkeepers.models import Goalkeeper


class GoalkeeperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goalkeeper
        fields = '__all__'
        depth = 2
