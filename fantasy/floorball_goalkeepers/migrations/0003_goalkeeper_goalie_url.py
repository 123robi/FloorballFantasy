# Generated by Django 3.1.1 on 2020-10-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floorball_goalkeepers', '0002_auto_20201004_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalkeeper',
            name='goalie_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
