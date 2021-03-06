# Generated by Django 3.1.2 on 2020-10-19 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('teams', '0004_team_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='captain_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='captain_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
