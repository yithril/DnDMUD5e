# Generated by Django 2.0.2 on 2018-03-31 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180331_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='desc',
        ),
    ]
