# Generated by Django 2.0.2 on 2018-04-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0033_auto_20180417_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='max_hp',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='max_mp',
            field=models.IntegerField(default=0),
        ),
    ]
