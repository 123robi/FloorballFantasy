from django.contrib.auth.models import User
from django.db import models

from fantasy.floorball_players.models import FloorballPlayer


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    players = models.ManyToManyField(FloorballPlayer)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
