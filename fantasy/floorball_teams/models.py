from django.db import models


class FloorballTeam(models.Model):
    name = models.CharField('Name', max_length=128)
    wins = models.PositiveIntegerField()
    loses = models.PositiveIntegerField()
    wins_after_over_time = models.PositiveIntegerField()
    loses_after_over_time = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    image_url = models.URLField(default='')
    team_url = models.URLField(default='')
    new_price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return self.name
