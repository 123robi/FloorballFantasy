from rest_framework import serializers

from teams.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')

    def create(self, validated_data):
        return Team.objects.create_user(**validated_data)
