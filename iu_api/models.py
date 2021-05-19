from django.db import models


# Каждый объект этого класса будет хранить данные об одной игровой сессии одного пользователя
class UserOnlineActivityObject(models.Model):
    steam_id = models.IntegerField()
    started_playing_time = models.DateTimeField()
    ended_playing_time = models.DateTimeField()
    game_id = models.IntegerField()
    total_played = models.FloatField()

