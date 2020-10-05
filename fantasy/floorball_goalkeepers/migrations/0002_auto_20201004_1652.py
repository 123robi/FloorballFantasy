# Generated by Django 3.1.1 on 2020-10-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floorball_goalkeepers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goalkeeper',
            old_name='conceded_goals',
            new_name='goals_conceded',
        ),
        migrations.AddField(
            model_name='goalkeeper',
            name='no_goals_conceded',
            field=models.PositiveIntegerField(default=0),
        ),
    ]