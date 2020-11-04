from rest_framework import serializers

from fantasy.common.exceptions import UserAlreadyHasTeam, TeamSizeException, BudgetException
from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.models import FloorballPlayer

from fantasy.teams.models import Team
from fantasy.users.serializer import UserSerializer


class TeamCreateSerializer(serializers.ModelSerializer):
    isCaptainGoalie = serializers.BooleanField(write_only=True)
    captainId = serializers.IntegerField(write_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'players', 'goalie', 'isCaptainGoalie', 'captainId', 'team_attack', 'team_defense']

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

        if validated_data.pop('isCaptainGoalie'):
            captain = Goalkeeper.objects.filter(id=validated_data.pop('captainId')).first()
        else:
            captain = FloorballPlayer.objects.filter(id=validated_data.pop('captainId')).first()

        validated_data['captain_object'] = captain
        validated_data['budget'] = budget

        return super().create(validated_data)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs


class TeamListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team_price = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['name', 'budget', 'points', 'user', 'team_price']
        depth = 1

    def get_team_price(self, obj):
        return sum(player.new_price for player in obj.players.all())


class TeamRetrieveSerializer(serializers.ModelSerializer):
    team_price = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()

    class Meta:
        model = Team
        exclude = ['user']
        depth = 2

    def get_team_price(self, obj):
        return sum(player.new_price for player in obj.players.all())

    def get_ranking(self, obj):
        return obj.ranking()
