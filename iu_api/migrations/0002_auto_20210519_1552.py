# Generated by Django 3.2.3 on 2021-05-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iu_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useronlineactivityobject',
            name='ended_playing_time',
        ),
        migrations.RemoveField(
            model_name='useronlineactivityobject',
            name='started_playing_time',
        ),
        migrations.AddField(
            model_name='useronlineactivityobject',
            name='ended_playing_timestamp',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useronlineactivityobject',
            name='started_playing_timestamp',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
