# Generated by Django 2.0.2 on 2018-04-17 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0031_auto_20180416_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='goodAlignment',
            field=models.IntegerField(choices=[(100, 'Good'), (50, 'Neutral'), (0, 'Evil')], default=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='lawfulAlignment',
            field=models.IntegerField(choices=[(100, 'Lawful'), (50, 'Neutral'), (0, 'Chaotic')], default=100),
        ),
    ]
