from django.db import models

from fantasy.floorball_teams.models import FloorballTeam


class Goalkeeper(models.Model):
    name = models.CharField('Name', max_length=128)
    games_played = models.PositiveIntegerField()
    shoots_on_goal = models.PositiveIntegerField()
    goals_conceded = models.PositiveIntegerField()
    no_goals_conceded = models.PositiveIntegerField(default=0)

    floorball_team = models.ForeignKey(FloorballTeam, related_name='goalkeepers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
