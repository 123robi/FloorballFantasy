# Generated by Django 3.1.2 on 2020-11-04 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floorball_teams', '0004_auto_20200928_1257'),
        ('teams', '0006_team_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_attack',
            field=models.ForeignKey(default=37, on_delete=django.db.models.deletion.CASCADE, related_name='team_team_attack', to='floorball_teams.floorballteam'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='team_defense',
            field=models.ForeignKey(default=37, on_delete=django.db.models.deletion.CASCADE, related_name='team_team_defense', to='floorball_teams.floorballteam'),
            preserve_default=False,
        ),
    ]
