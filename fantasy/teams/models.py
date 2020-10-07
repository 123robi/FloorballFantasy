from django.contrib.auth.models import User
from django.db import models

from fantasy.floorball_goalkeepers.models import Goalkeeper
from fantasy.floorball_players.models import FloorballPlayer


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(FloorballPlayer)
    budget = models.IntegerField(default=1000000)
    goalie = models.ForeignKey(Goalkeeper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
