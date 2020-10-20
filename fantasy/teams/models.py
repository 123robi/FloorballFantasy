from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Count

from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.models import FloorballPlayer


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(FloorballPlayer)
    budget = models.IntegerField(default=1000000)
    goalie = models.ForeignKey(Goalkeeper, on_delete=models.CASCADE)
    captain_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    captain_id = models.PositiveIntegerField(null=True)
    captain_object = GenericForeignKey('captain_type', 'captain_id')
    points = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def ranking(self):
        aggregate = Team.objects.filter(points__gt=self.points).aggregate(ranking=Count('points'))
        return aggregate['ranking'] + 1
