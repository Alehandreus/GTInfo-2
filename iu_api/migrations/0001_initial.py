# Generated by Django 3.2.3 on 2021-05-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserOnlineActivityObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_id', models.IntegerField()),
                ('started_playing_time', models.DateTimeField()),
                ('ended_playing_time', models.DateTimeField()),
                ('game_id', models.IntegerField()),
                ('total_played', models.FloatField()),
            ],
        ),
    ]
