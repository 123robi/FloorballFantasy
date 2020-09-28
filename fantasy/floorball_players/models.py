from django.db import models

from fantasy.floorball_teams.models import FloorballTeam


class FloorballPlayer(models.Model):
    name = models.CharField('Name', max_length=128)
    games_played = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    penalties = models.PositiveIntegerField()
    plus_minus = models.IntegerField()

    team = models.ForeignKey(FloorballTeam, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
