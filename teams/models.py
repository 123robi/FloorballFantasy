from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField('Name', max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
