# Generated by Django 2.0.2 on 2018-04-26 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0038_guild_main_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(default='')),
                ('name', models.CharField(max_length=100)),
                ('guild', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='game.Guild')),
                ('race', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='game.Race')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CharAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Ability')),
            ],
        ),
        migrations.CreateModel(
            name='CharBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Achievement')),
            ],
        ),
        migrations.CreateModel(
            name='CharQuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_finished', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='proficiency_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='charquest',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Character'),
        ),
        migrations.AddField(
            model_name='charbadge',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Character'),
        ),
        migrations.AddField(
            model_name='charability',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Character'),
        ),
    ]
