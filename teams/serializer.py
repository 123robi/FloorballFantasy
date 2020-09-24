from rest_framework import serializers

from teams.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs
