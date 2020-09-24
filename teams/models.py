from django.db import models

class Team(models.Model):
    name = models.CharField('Name', max_length=128)

class Test:
    pass
