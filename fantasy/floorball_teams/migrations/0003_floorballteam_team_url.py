# Generated by Django 3.1.1 on 2020-09-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floorball_teams', '0002_floorballteam_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='floorballteam',
            name='team_url',
            field=models.URLField(default=''),
        ),
    ]
