from rest_framework import serializers

from fantasy.common.exceptions import UserAlreadyHasTeam, TeamSizeException, BudgetException

from fantasy.teams.models import Team


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'players', 'goalie')

    def create(self, validated_data):
        budget = 1000000
        if Team.objects.filter(user=validated_data['user']).count() != 0:
            raise UserAlreadyHasTeam

        players = validated_data.get('players', [])
        if len(players) != 5:
            raise TeamSizeException

        for player in players:
            budget -= player.new_price

        if budget < 0:
            raise BudgetException

        validated_data['budget'] = budget

        return super().create(validated_data)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs


class TeamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['user']
        depth = 2
