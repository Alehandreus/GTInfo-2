from django.db import models


# Каждый объект этого класса будет хранить данные об одном пользователе с его параметрами и списком игровых сессий
class TrackedUserObject(models.Model):
    steam_id = models.IntegerField(unique=True, primary_key=True, null=False)

    def __str__(self):
        return str(self.steam_id)


# Каждый объект этого класса будет хранить данные об одной игровой сессии одного пользователя
class UserOnlineActivityObject(models.Model):
    tracked_user = models.ForeignKey(TrackedUserObject, on_delete=models.CASCADE, related_name="sessions",
                                     to_field="steam_id")
    started_playing_timestamp = models.IntegerField()
    ended_playing_timestamp = models.IntegerField()
    game_id = models.IntegerField()
    total_played = models.FloatField()



