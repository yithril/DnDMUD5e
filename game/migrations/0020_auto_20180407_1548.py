# Generated by Django 2.0.2 on 2018-04-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_auto_20180407_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='skill_points',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='race',
            name='skill_points',
            field=models.IntegerField(default=0),
        ),
    ]
