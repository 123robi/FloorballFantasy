# Generated by Django 3.1.1 on 2020-09-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floorball_players', '0003_auto_20200930_1101'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='floorball_players.FloorballPlayer'),
        ),
    ]
